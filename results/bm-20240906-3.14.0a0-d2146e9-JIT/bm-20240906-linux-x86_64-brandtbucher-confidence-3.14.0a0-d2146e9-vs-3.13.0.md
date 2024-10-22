# Results vs. 3.13.0

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d2146e9
- commit date: 2024-09-06
- overall geometric mean: 1.00x faster
- HPT reliability: 88.31%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                              |
| docutils       | 2.58 sec                                               | 3.00 sec: 1.16x slower                                            |
| html5lib       | 64.5 ms                                                | 62.3 ms: 1.04x faster                                             |
| tornado_http   | 91.5 ms                                                | 96.1 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 407 ms: 1.14x faster                                              |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                              |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                              |
| async_tree_none_tg        | 320 ms                                                 | 313 ms: 1.02x faster                                              |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 568 ms: 1.01x faster                                              |
| asyncio_tcp               | 488 ms                                                 | 486 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                             |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                              |
| async_tree_io_tg          | 825 ms                                                 | 893 ms: 1.08x slower                                              |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                              |
| Geometric mean            | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.7 ms: 1.11x faster                                             |
| nbody          | 85.7 ms                                                | 81.2 ms: 1.06x faster                                             |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.50 ms: 1.11x faster                                             |
| regex_v8       | 25.3 ms                                                | 24.0 ms: 1.05x faster                                             |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                              |
| regex_compile  | 131 ms                                                 | 142 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 78.3 ms: 1.11x faster                                             |
| tomli_loads         | 2.11 sec                                               | 1.93 sec: 1.10x faster                                            |
| xml_etree_process   | 60.4 ms                                                | 55.1 ms: 1.10x faster                                             |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.06x faster                                              |
| xml_etree_iterparse | 102 ms                                                 | 98.8 ms: 1.03x faster                                             |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| pickle              | 11.6 us                                                | 11.6 us: 1.00x slower                                             |
| pickle_pure_python  | 300 us                                                 | 304 us: 1.01x slower                                              |
| pickle_dict         | 33.2 us                                                | 34.1 us: 1.03x slower                                             |
| pickle_list         | 5.01 us                                                | 5.29 us: 1.06x slower                                             |
| json_loads          | 27.0 us                                                | 28.6 us: 1.06x slower                                             |
| unpickle_list       | 4.96 us                                                | 5.40 us: 1.09x slower                                             |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                      |

Benchmark hidden because not significant (2): unpickle, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                             |
| python_startup_no_site | 6.99 ms                                                | 7.16 ms: 1.03x slower                                             |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.79 ms: 1.13x faster                                             |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                             |
| genshi_text     | 22.9 ms                                                | 24.4 ms: 1.07x slower                                             |
| genshi_xml      | 50.3 ms                                                | 58.7 ms: 1.17x slower                                             |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|---------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.0 us: 1.41x faster                                             |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                              |
| richards_super            | 54.4 ms                                                | 42.9 ms: 1.27x faster                                             |
| richards                  | 48.1 ms                                                | 38.7 ms: 1.24x faster                                             |
| scimark_fft               | 369 ms                                                 | 312 ms: 1.18x faster                                              |
| deepcopy_reduce           | 3.17 us                                                | 2.70 us: 1.18x faster                                             |
| async_tree_memoization_tg | 465 ms                                                 | 407 ms: 1.14x faster                                              |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.43 ms: 1.14x faster                                             |
| mako                      | 11.1 ms                                                | 9.79 ms: 1.13x faster                                             |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                              |
| async_tree_memoization    | 442 ms                                                 | 396 ms: 1.12x faster                                              |
| regex_effbot              | 3.88 ms                                                | 3.50 ms: 1.11x faster                                             |
| xml_etree_generate        | 87.0 ms                                                | 78.3 ms: 1.11x faster                                             |
| float                     | 78.5 ms                                                | 70.7 ms: 1.11x faster                                             |
| crypto_pyaes              | 73.0 ms                                                | 66.4 ms: 1.10x faster                                             |
| tomli_loads               | 2.11 sec                                               | 1.93 sec: 1.10x faster                                            |
| xml_etree_process         | 60.4 ms                                                | 55.1 ms: 1.10x faster                                             |
| async_tree_none           | 354 ms                                                 | 326 ms: 1.09x faster                                              |
| pyflate                   | 460 ms                                                 | 424 ms: 1.08x faster                                              |
| go                        | 142 ms                                                 | 131 ms: 1.08x faster                                              |
| telco                     | 8.45 ms                                                | 7.83 ms: 1.08x faster                                             |
| pathlib                   | 17.1 ms                                                | 16.0 ms: 1.07x faster                                             |
| pprint_safe_repr          | 744 ms                                                 | 700 ms: 1.06x faster                                              |
| scimark_sor               | 122 ms                                                 | 116 ms: 1.06x faster                                              |
| bpe_tokeniser             | 4.69 sec                                               | 4.43 sec: 1.06x faster                                            |
| xml_etree_parse           | 156 ms                                                 | 148 ms: 1.06x faster                                              |
| nbody                     | 85.7 ms                                                | 81.2 ms: 1.06x faster                                             |
| regex_v8                  | 25.3 ms                                                | 24.0 ms: 1.05x faster                                             |
| scimark_monte_carlo       | 66.3 ms                                                | 62.9 ms: 1.05x faster                                             |
| regex_dna                 | 220 ms                                                 | 210 ms: 1.05x faster                                              |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                              |
| pprint_pformat            | 1.51 sec                                               | 1.46 sec: 1.04x faster                                            |
| html5lib                  | 64.5 ms                                                | 62.3 ms: 1.04x faster                                             |
| xml_etree_iterparse       | 102 ms                                                 | 98.8 ms: 1.03x faster                                             |
| sqlite_synth              | 2.85 us                                                | 2.77 us: 1.03x faster                                             |
| logging_simple            | 5.66 us                                                | 5.52 us: 1.03x faster                                             |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.03x faster                                              |
| async_tree_none_tg        | 320 ms                                                 | 313 ms: 1.02x faster                                              |
| logging_format            | 6.25 us                                                | 6.12 us: 1.02x faster                                             |
| pycparser                 | 1.19 sec                                               | 1.18 sec: 1.02x faster                                            |
| thrift                    | 796 us                                                 | 787 us: 1.01x faster                                              |
| async_tree_cpu_io_mixed   | 574 ms                                                 | 568 ms: 1.01x faster                                              |
| logging_silent            | 102 ns                                                 | 101 ns: 1.01x faster                                              |
| gc_traversal              | 3.81 ms                                                | 3.77 ms: 1.01x faster                                             |
| json_dumps                | 10.4 ms                                                | 10.3 ms: 1.01x faster                                             |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| asyncio_tcp               | 488 ms                                                 | 486 ms: 1.00x faster                                              |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                              |
| mdp                       | 2.74 sec                                               | 2.73 sec: 1.00x faster                                            |
| pickle                    | 11.6 us                                                | 11.6 us: 1.00x slower                                             |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.80 sec: 1.01x slower                                            |
| python_startup            | 10.6 ms                                                | 10.7 ms: 1.01x slower                                             |
| coroutines                | 22.5 ms                                                | 22.7 ms: 1.01x slower                                             |
| pickle_pure_python        | 300 us                                                 | 304 us: 1.01x slower                                              |
| comprehensions            | 16.4 us                                                | 16.6 us: 1.01x slower                                             |
| deltablue                 | 3.15 ms                                                | 3.20 ms: 1.02x slower                                             |
| python_startup_no_site    | 6.99 ms                                                | 7.16 ms: 1.03x slower                                             |
| pickle_dict               | 33.2 us                                                | 34.1 us: 1.03x slower                                             |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                              |
| bench_thread_pool         | 815 us                                                 | 839 us: 1.03x slower                                              |
| json                      | 5.20 ms                                                | 5.35 ms: 1.03x slower                                             |
| django_template           | 34.4 ms                                                | 35.5 ms: 1.03x slower                                             |
| coverage                  | 83.7 ms                                                | 86.8 ms: 1.04x slower                                             |
| 2to3                      | 265 ms                                                 | 276 ms: 1.04x slower                                              |
| sqlglot_normalize         | 107 ms                                                 | 112 ms: 1.05x slower                                              |
| tornado_http              | 91.5 ms                                                | 96.1 ms: 1.05x slower                                             |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                              |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                             |
| nqueens                   | 80.6 ms                                                | 85.1 ms: 1.06x slower                                             |
| pickle_list               | 5.01 us                                                | 5.29 us: 1.06x slower                                             |
| json_loads                | 27.0 us                                                | 28.6 us: 1.06x slower                                             |
| async_generators          | 433 ms                                                 | 459 ms: 1.06x slower                                              |
| genshi_text               | 22.9 ms                                                | 24.4 ms: 1.07x slower                                             |
| sqlglot_transpile         | 1.57 ms                                                | 1.68 ms: 1.07x slower                                             |
| async_tree_io_tg          | 825 ms                                                 | 893 ms: 1.08x slower                                              |
| sqlglot_optimize          | 53.9 ms                                                | 58.3 ms: 1.08x slower                                             |
| regex_compile             | 131 ms                                                 | 142 ms: 1.08x slower                                              |
| unpickle_list             | 4.96 us                                                | 5.40 us: 1.09x slower                                             |
| create_gc_cycles          | 1.61 ms                                                | 1.77 ms: 1.10x slower                                             |
| dulwich_log               | 63.0 ms                                                | 69.4 ms: 1.10x slower                                             |
| async_tree_io             | 843 ms                                                 | 929 ms: 1.10x slower                                              |
| sympy_str                 | 274 ms                                                 | 302 ms: 1.10x slower                                              |
| sympy_expand              | 462 ms                                                 | 511 ms: 1.11x slower                                              |
| hexiom                    | 6.13 ms                                                | 6.84 ms: 1.12x slower                                             |
| sympy_integrate           | 19.9 ms                                                | 22.8 ms: 1.15x slower                                             |
| generators                | 28.8 ms                                                | 33.2 ms: 1.15x slower                                             |
| docutils                  | 2.58 sec                                               | 3.00 sec: 1.16x slower                                            |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.16x slower                                              |
| genshi_xml                | 50.3 ms                                                | 58.7 ms: 1.17x slower                                             |
| pylint                    | 313 ms                                                 | 373 ms: 1.19x slower                                              |
| unpack_sequence           | 42.4 ns                                                | 109 ns: 2.57x slower                                              |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                      |

Benchmark hidden because not significant (6): unpickle, chaos, unpickle_pure_python, bench_mp_pool, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 88.31% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x