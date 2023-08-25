
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 264 ms: 1.28x faster                                  |
| chameleon      | 9.06 ms                                                | 7.44 ms: 1.22x faster                                 |
| html5lib       | 85.9 ms                                                | 68.5 ms: 1.25x faster                                 |
| tornado_http   | 127 ms                                                 | 108 ms: 1.18x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 96.1 ms: 1.47x faster                                 |
| float          | 111 ms                                                 | 79.2 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 139 ms: 1.27x faster                                  |
| regex_dna      | 222 ms                                                 | 212 ms: 1.05x faster                                  |
| regex_v8       | 25.0 ms                                                | 24.5 ms: 1.02x faster                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 347 us: 1.31x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 57.8 ms: 1.30x faster                                 |
| unpickle_pure_python | 300 us                                                 | 251 us: 1.20x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.8 ms: 1.17x faster                                 |
| json_loads           | 28.8 us                                                | 25.6 us: 1.12x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.07x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| pickle               | 10.3 us                                                | 9.95 us: 1.03x faster                                 |
| pickle_dict          | 27.3 us                                                | 27.7 us: 1.02x slower                                 |
| pickle_list          | 4.56 us                                                | 4.68 us: 1.03x slower                                 |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                 |
| unpickle_list        | 4.82 us                                                | 5.21 us: 1.08x slower                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.00 ms: 1.77x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 5.78 ms: 1.01x faster                                 |
| Geometric mean         | (ref)                                                  | 1.33x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 45.9 ms                                                | 36.5 ms: 1.26x faster                                 |
| mako            | 14.8 ms                                                | 11.9 ms: 1.24x faster                                 |
| Geometric mean  | (ref)                                                  | 1.25x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup          | 14.2 ms                                                | 8.00 ms: 1.77x faster                                 |
| deltablue               | 7.42 ms                                                | 4.54 ms: 1.63x faster                                 |
| logging_silent          | 175 ns                                                 | 110 ns: 1.59x faster                                  |
| scimark_sor             | 197 ms                                                 | 130 ms: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 96.1 ms: 1.47x faster                                 |
| scimark_monte_carlo     | 108 ms                                                 | 74.0 ms: 1.46x faster                                 |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.46x faster                                  |
| go                      | 229 ms                                                 | 158 ms: 1.45x faster                                  |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.45x faster                                  |
| chaos                   | 106 ms                                                 | 73.9 ms: 1.44x faster                                 |
| pyflate                 | 673 ms                                                 | 477 ms: 1.41x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.77 ms: 1.41x faster                                 |
| float                   | 111 ms                                                 | 79.2 ms: 1.40x faster                                 |
| raytrace                | 464 ms                                                 | 333 ms: 1.39x faster                                  |
| richards                | 74.9 ms                                                | 54.5 ms: 1.37x faster                                 |
| logging_format          | 8.91 us                                                | 6.49 us: 1.37x faster                                 |
| logging_simple          | 8.07 us                                                | 5.97 us: 1.35x faster                                 |
| crypto_pyaes            | 118 ms                                                 | 88.1 ms: 1.34x faster                                 |
| unpack_sequence         | 64.7 ns                                                | 49.2 ns: 1.32x faster                                 |
| pickle_pure_python      | 455 us                                                 | 347 us: 1.31x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 57.8 ms: 1.30x faster                                 |
| 2to3                    | 336 ms                                                 | 264 ms: 1.28x faster                                  |
| regex_compile           | 177 ms                                                 | 139 ms: 1.27x faster                                  |
| scimark_fft             | 424 ms                                                 | 332 ms: 1.27x faster                                  |
| thrift                  | 1.03 ms                                                | 814 us: 1.27x faster                                  |
| fannkuch                | 486 ms                                                 | 386 ms: 1.26x faster                                  |
| django_template         | 45.9 ms                                                | 36.5 ms: 1.26x faster                                 |
| html5lib                | 85.9 ms                                                | 68.5 ms: 1.25x faster                                 |
| mako                    | 14.8 ms                                                | 11.9 ms: 1.24x faster                                 |
| chameleon               | 9.06 ms                                                | 7.44 ms: 1.22x faster                                 |
| pycparser               | 1.50 sec                                               | 1.24 sec: 1.21x faster                                |
| unpickle_pure_python    | 300 us                                                 | 251 us: 1.20x faster                                  |
| nqueens                 | 100 ms                                                 | 84.6 ms: 1.18x faster                                 |
| tornado_http            | 127 ms                                                 | 108 ms: 1.18x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.8 ms: 1.17x faster                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.77 ms: 1.14x faster                                 |
| dulwich_log             | 75.9 ms                                                | 67.2 ms: 1.13x faster                                 |
| json_loads              | 28.8 us                                                | 25.6 us: 1.12x faster                                 |
| json                    | 5.42 ms                                                | 4.83 ms: 1.12x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 21.7 ms: 1.12x faster                                 |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                  |
| sympy_sum               | 185 ms                                                 | 172 ms: 1.07x faster                                  |
| json_dumps              | 13.5 ms                                                | 12.6 ms: 1.07x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.74 us: 1.07x faster                                 |
| sympy_expand            | 545 ms                                                 | 509 ms: 1.07x faster                                  |
| sympy_str               | 328 ms                                                 | 308 ms: 1.07x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                  |
| regex_dna               | 222 ms                                                 | 212 ms: 1.05x faster                                  |
| pickle                  | 10.3 us                                                | 9.95 us: 1.03x faster                                 |
| pathlib                 | 20.0 ms                                                | 19.4 ms: 1.03x faster                                 |
| regex_v8                | 25.0 ms                                                | 24.5 ms: 1.02x faster                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.78 ms: 1.01x faster                                 |
| pickle_dict             | 27.3 us                                                | 27.7 us: 1.02x slower                                 |
| pickle_list             | 4.56 us                                                | 4.68 us: 1.03x slower                                 |
| unpickle                | 14.1 us                                                | 14.6 us: 1.03x slower                                 |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.21 us: 1.08x slower                                 |
| Geometric mean          | (ref)                                                  | 1.21x faster                                          |

Benchmark hidden because not significant (2): regex_effbot, telco
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.15x
