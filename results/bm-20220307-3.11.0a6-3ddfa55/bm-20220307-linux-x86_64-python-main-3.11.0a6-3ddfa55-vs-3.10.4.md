
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                  |
| chameleon      | 9.06 ms                                                | 6.93 ms: 1.31x faster                                 |
| html5lib       | 85.9 ms                                                | 68.6 ms: 1.25x faster                                 |
| tornado_http   | 127 ms                                                 | 99.2 ms: 1.28x faster                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 142 ms                                                 | 97.7 ms: 1.45x faster                                 |
| float          | 111 ms                                                 | 78.7 ms: 1.40x faster                                 |
| pidigits       | 190 ms                                                 | 208 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 140 ms: 1.27x faster                                  |
| regex_v8       | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| regex_dna      | 222 ms                                                 | 221 ms: 1.00x faster                                  |
| regex_effbot   | 3.23 ms                                                | 3.49 ms: 1.08x slower                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 335 us: 1.36x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                 |
| unpickle_pure_python | 300 us                                                 | 246 us: 1.22x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 79.6 ms: 1.18x faster                                 |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.07x faster                                 |
| pickle               | 10.3 us                                                | 9.69 us: 1.06x faster                                 |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                  |
| json_loads           | 28.8 us                                                | 28.1 us: 1.03x faster                                 |
| pickle_list          | 4.56 us                                                | 4.51 us: 1.01x faster                                 |
| unpickle_list        | 4.82 us                                                | 4.92 us: 1.02x slower                                 |
| pickle_dict          | 27.3 us                                                | 28.1 us: 1.03x slower                                 |
| Geometric mean       | (ref)                                                  | 1.10x faster                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.20 ms: 1.73x faster                                 |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                 |
| Geometric mean         | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.6 ms: 1.39x faster                                 |
| django_template | 45.9 ms                                                | 36.0 ms: 1.28x faster                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 4.16 ms: 1.78x faster                                 |
| python_startup          | 14.2 ms                                                | 8.20 ms: 1.73x faster                                 |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.59x faster                                  |
| go                      | 229 ms                                                 | 148 ms: 1.55x faster                                  |
| logging_silent          | 175 ns                                                 | 113 ns: 1.55x faster                                  |
| richards                | 74.9 ms                                                | 48.5 ms: 1.54x faster                                 |
| pyflate                 | 673 ms                                                 | 453 ms: 1.49x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 72.9 ms: 1.48x faster                                 |
| logging_format          | 8.91 us                                                | 6.08 us: 1.46x faster                                 |
| logging_simple          | 8.07 us                                                | 5.52 us: 1.46x faster                                 |
| raytrace                | 464 ms                                                 | 318 ms: 1.46x faster                                  |
| nbody                   | 142 ms                                                 | 97.7 ms: 1.45x faster                                 |
| chaos                   | 106 ms                                                 | 73.5 ms: 1.45x faster                                 |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.41x faster                                  |
| float                   | 111 ms                                                 | 78.7 ms: 1.40x faster                                 |
| crypto_pyaes            | 118 ms                                                 | 84.6 ms: 1.40x faster                                 |
| spectral_norm           | 150 ms                                                 | 107 ms: 1.40x faster                                  |
| mako                    | 14.8 ms                                                | 10.6 ms: 1.39x faster                                 |
| pickle_pure_python      | 455 us                                                 | 335 us: 1.36x faster                                  |
| hexiom                  | 9.53 ms                                                | 7.04 ms: 1.35x faster                                 |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                 |
| thrift                  | 1.03 ms                                                | 789 us: 1.31x faster                                  |
| chameleon               | 9.06 ms                                                | 6.93 ms: 1.31x faster                                 |
| tornado_http            | 127 ms                                                 | 99.2 ms: 1.28x faster                                 |
| django_template         | 45.9 ms                                                | 36.0 ms: 1.28x faster                                 |
| regex_compile           | 177 ms                                                 | 140 ms: 1.27x faster                                  |
| scimark_fft             | 424 ms                                                 | 336 ms: 1.26x faster                                  |
| 2to3                    | 336 ms                                                 | 268 ms: 1.26x faster                                  |
| html5lib                | 85.9 ms                                                | 68.6 ms: 1.25x faster                                 |
| pycparser               | 1.50 sec                                               | 1.21 sec: 1.24x faster                                |
| unpickle_pure_python    | 300 us                                                 | 246 us: 1.22x faster                                  |
| fannkuch                | 486 ms                                                 | 398 ms: 1.22x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 79.6 ms: 1.18x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.51 us: 1.17x faster                                 |
| sympy_integrate         | 24.3 ms                                                | 20.9 ms: 1.16x faster                                 |
| nqueens                 | 100 ms                                                 | 87.0 ms: 1.15x faster                                 |
| dulwich_log             | 75.9 ms                                                | 66.5 ms: 1.14x faster                                 |
| sympy_str               | 328 ms                                                 | 289 ms: 1.14x faster                                  |
| sympy_expand            | 545 ms                                                 | 481 ms: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.82 ms: 1.13x faster                                 |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                 |
| regex_v8                | 25.0 ms                                                | 23.0 ms: 1.09x faster                                 |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.09x faster                                  |
| json                    | 5.42 ms                                                | 5.00 ms: 1.08x faster                                 |
| json_dumps              | 13.5 ms                                                | 12.6 ms: 1.07x faster                                 |
| pickle                  | 10.3 us                                                | 9.69 us: 1.06x faster                                 |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.04x faster                                  |
| json_loads              | 28.8 us                                                | 28.1 us: 1.03x faster                                 |
| pickle_list             | 4.56 us                                                | 4.51 us: 1.01x faster                                 |
| regex_dna               | 222 ms                                                 | 221 ms: 1.00x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.92 us: 1.02x slower                                 |
| pickle_dict             | 27.3 us                                                | 28.1 us: 1.03x slower                                 |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                 |
| telco                   | 6.54 ms                                                | 6.92 ms: 1.06x slower                                 |
| regex_effbot            | 3.23 ms                                                | 3.49 ms: 1.08x slower                                 |
| pidigits                | 190 ms                                                 | 208 ms: 1.10x slower                                  |
| unpack_sequence         | 64.7 ns                                                | 131 ns: 2.02x slower                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                          |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (40) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x
