
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 264 ms: 1.27x faster                                  |
| chameleon      | 9.06 ms                                                | 6.87 ms: 1.32x faster                                 |
| html5lib       | 85.9 ms                                                | 65.3 ms: 1.32x faster                                 |
| tornado_http   | 127 ms                                                 | 95.4 ms: 1.34x faster                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 95.2 ms: 1.49x faster                                 |
| float          | 111 ms                                                 | 74.4 ms: 1.49x faster                                 |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.34 ms: 1.03x slower                                 |
| regex_v8       | 25.0 ms                                                | 25.9 ms: 1.03x slower                                 |
| regex_dna      | 222 ms                                                 | 231 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.46x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 55.2 ms: 1.36x faster                                 |
| unpickle_pure_python | 300 us                                                 | 231 us: 1.30x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 78.5 ms: 1.20x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.5 ms: 1.08x faster                                 |
| pickle               | 10.3 us                                                | 9.55 us: 1.08x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| json_loads           | 28.8 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict          | 27.3 us                                                | 27.6 us: 1.01x slower                                 |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                 |
| Geometric mean       | (ref)                                                  | 1.11x faster                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.07 ms: 1.75x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 5.98 ms: 1.03x slower                                 |
| Geometric mean         | (ref)                                                  | 1.31x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.2 ms: 1.45x faster                                 |
| django_template | 45.9 ms                                                | 34.3 ms: 1.34x faster                                 |
| Geometric mean  | (ref)                                                  | 1.39x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.70 ms: 2.01x faster                                 |
| python_startup          | 14.2 ms                                                | 8.07 ms: 1.75x faster                                 |
| logging_silent          | 175 ns                                                 | 104 ns: 1.69x faster                                  |
| go                      | 229 ms                                                 | 143 ms: 1.61x faster                                  |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.60x faster                                  |
| richards                | 74.9 ms                                                | 47.5 ms: 1.58x faster                                 |
| pyflate                 | 673 ms                                                 | 438 ms: 1.54x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 70.8 ms: 1.53x faster                                 |
| raytrace                | 464 ms                                                 | 306 ms: 1.52x faster                                  |
| chaos                   | 106 ms                                                 | 70.2 ms: 1.51x faster                                 |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                  |
| nbody                   | 142 ms                                                 | 95.2 ms: 1.49x faster                                 |
| float                   | 111 ms                                                 | 74.4 ms: 1.49x faster                                 |
| pickle_pure_python      | 455 us                                                 | 311 us: 1.46x faster                                  |
| mako                    | 14.8 ms                                                | 10.2 ms: 1.45x faster                                 |
| unpack_sequence         | 64.7 ns                                                | 44.9 ns: 1.44x faster                                 |
| spectral_norm           | 150 ms                                                 | 105 ms: 1.44x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 82.7 ms: 1.43x faster                                 |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                 |
| hexiom                  | 9.53 ms                                                | 6.84 ms: 1.39x faster                                 |
| logging_simple          | 8.07 us                                                | 5.80 us: 1.39x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 55.2 ms: 1.36x faster                                 |
| thrift                  | 1.03 ms                                                | 762 us: 1.36x faster                                  |
| django_template         | 45.9 ms                                                | 34.3 ms: 1.34x faster                                 |
| tornado_http            | 127 ms                                                 | 95.4 ms: 1.34x faster                                 |
| chameleon               | 9.06 ms                                                | 6.87 ms: 1.32x faster                                 |
| html5lib                | 85.9 ms                                                | 65.3 ms: 1.32x faster                                 |
| unpickle_pure_python    | 300 us                                                 | 231 us: 1.30x faster                                  |
| regex_compile           | 177 ms                                                 | 137 ms: 1.29x faster                                  |
| 2to3                    | 336 ms                                                 | 264 ms: 1.27x faster                                  |
| scimark_fft             | 424 ms                                                 | 335 ms: 1.26x faster                                  |
| fannkuch                | 486 ms                                                 | 401 ms: 1.21x faster                                  |
| pycparser               | 1.50 sec                                               | 1.24 sec: 1.21x faster                                |
| xml_etree_generate      | 94.2 ms                                                | 78.5 ms: 1.20x faster                                 |
| dulwich_log             | 75.9 ms                                                | 63.8 ms: 1.19x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.19x faster                                 |
| nqueens                 | 100 ms                                                 | 85.2 ms: 1.17x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.51 us: 1.17x faster                                 |
| sympy_sum               | 185 ms                                                 | 160 ms: 1.15x faster                                  |
| sympy_expand            | 545 ms                                                 | 476 ms: 1.14x faster                                  |
| sympy_str               | 328 ms                                                 | 287 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.85 ms: 1.12x faster                                 |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                 |
| json_dumps              | 13.5 ms                                                | 12.5 ms: 1.08x faster                                 |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.08x faster                                  |
| pickle                  | 10.3 us                                                | 9.55 us: 1.08x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                  |
| json                    | 5.42 ms                                                | 5.07 ms: 1.07x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 157 ms: 1.04x faster                                  |
| json_loads              | 28.8 us                                                | 28.1 us: 1.02x faster                                 |
| pickle_dict             | 27.3 us                                                | 27.6 us: 1.01x slower                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.98 ms: 1.03x slower                                 |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                 |
| regex_effbot            | 3.23 ms                                                | 3.34 ms: 1.03x slower                                 |
| regex_v8                | 25.0 ms                                                | 25.9 ms: 1.03x slower                                 |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                  |
| regex_dna               | 222 ms                                                 | 231 ms: 1.04x slower                                  |
| Geometric mean          | (ref)                                                  | 1.26x faster                                          |

Benchmark hidden because not significant (3): unpickle, pickle_list, telco
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
