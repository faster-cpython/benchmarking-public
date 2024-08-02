# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.00x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 303 ms                                                                      | 307 ms: 1.01x slower                                                        |
| docutils       | 3.10 sec                                                                    | 3.13 sec: 1.01x slower                                                      |
| html5lib       | 72.5 ms                                                                     | 73.9 ms: 1.02x slower                                                       |
| tornado_http   | 121 ms                                                                      | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.9 ms                                                                     | 74.6 ms: 1.00x faster                                                       |
| pidigits       | 251 ms                                                                      | 250 ms: 1.00x faster                                                        |
| nbody          | 83.4 ms                                                                     | 84.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 255 ms                                                                      | 242 ms: 1.05x faster                                                        |
| regex_v8       | 26.2 ms                                                                     | 25.8 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_dict          | 33.6 us                                                                     | 32.1 us: 1.05x faster                                                       |
| unpickle             | 15.6 us                                                                     | 15.5 us: 1.01x faster                                                       |
| pickle_list          | 4.55 us                                                                     | 4.53 us: 1.01x faster                                                       |
| xml_etree_process    | 58.0 ms                                                                     | 58.3 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 98.9 ms                                                                     | 99.7 ms: 1.01x slower                                                       |
| tomli_loads          | 2.11 sec                                                                    | 2.15 sec: 1.02x slower                                                      |
| unpickle_pure_python | 217 us                                                                      | 222 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (7): unpickle_list, json_dumps, xml_etree_parse, pickle, xml_etree_generate, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 41.3 ms                                                                     | 40.9 ms: 1.01x faster                                                       |
| mako            | 9.16 ms                                                                     | 9.24 ms: 1.01x slower                                                       |
| genshi_xml      | 63.9 ms                                                                     | 64.9 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240618-pythonperf2-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna                | 255 ms                                                                      | 242 ms: 1.05x faster                                                        |
| pickle_dict              | 33.6 us                                                                     | 32.1 us: 1.05x faster                                                       |
| pyflate                  | 461 ms                                                                      | 447 ms: 1.03x faster                                                        |
| chaos                    | 67.1 ms                                                                     | 65.9 ms: 1.02x faster                                                       |
| telco                    | 8.21 ms                                                                     | 8.06 ms: 1.02x faster                                                       |
| comprehensions           | 18.4 us                                                                     | 18.1 us: 1.02x faster                                                       |
| deepcopy_memo            | 28.8 us                                                                     | 28.3 us: 1.02x faster                                                       |
| logging_silent           | 104 ns                                                                      | 102 ns: 1.02x faster                                                        |
| regex_v8                 | 26.2 ms                                                                     | 25.8 ms: 1.01x faster                                                       |
| django_template          | 41.3 ms                                                                     | 40.9 ms: 1.01x faster                                                       |
| hexiom                   | 6.74 ms                                                                     | 6.68 ms: 1.01x faster                                                       |
| sqlglot_transpile        | 1.83 ms                                                                     | 1.81 ms: 1.01x faster                                                       |
| generators               | 34.3 ms                                                                     | 34.0 ms: 1.01x faster                                                       |
| async_generators         | 389 ms                                                                      | 386 ms: 1.01x faster                                                        |
| thrift                   | 902 us                                                                      | 896 us: 1.01x faster                                                        |
| unpickle                 | 15.6 us                                                                     | 15.5 us: 1.01x faster                                                       |
| pickle_list              | 4.55 us                                                                     | 4.53 us: 1.01x faster                                                       |
| float                    | 74.9 ms                                                                     | 74.6 ms: 1.00x faster                                                       |
| pathlib                  | 16.2 ms                                                                     | 16.1 ms: 1.00x faster                                                       |
| pidigits                 | 251 ms                                                                      | 250 ms: 1.00x faster                                                        |
| meteor_contest           | 130 ms                                                                      | 131 ms: 1.00x slower                                                        |
| scimark_monte_carlo      | 66.1 ms                                                                     | 66.4 ms: 1.00x slower                                                       |
| sympy_str                | 312 ms                                                                      | 314 ms: 1.00x slower                                                        |
| xml_etree_process        | 58.0 ms                                                                     | 58.3 ms: 1.01x slower                                                       |
| richards                 | 45.5 ms                                                                     | 45.8 ms: 1.01x slower                                                       |
| xml_etree_iterparse      | 98.9 ms                                                                     | 99.7 ms: 1.01x slower                                                       |
| mako                     | 9.16 ms                                                                     | 9.24 ms: 1.01x slower                                                       |
| go                       | 160 ms                                                                      | 162 ms: 1.01x slower                                                        |
| sqlite_synth             | 2.76 us                                                                     | 2.79 us: 1.01x slower                                                       |
| sympy_expand             | 524 ms                                                                      | 529 ms: 1.01x slower                                                        |
| gc_traversal             | 4.42 ms                                                                     | 4.47 ms: 1.01x slower                                                       |
| sqlglot_optimize         | 63.1 ms                                                                     | 63.7 ms: 1.01x slower                                                       |
| dulwich_log              | 65.6 ms                                                                     | 66.3 ms: 1.01x slower                                                       |
| coroutines               | 21.6 ms                                                                     | 21.9 ms: 1.01x slower                                                       |
| 2to3                     | 303 ms                                                                      | 307 ms: 1.01x slower                                                        |
| docutils                 | 3.10 sec                                                                    | 3.13 sec: 1.01x slower                                                      |
| scimark_fft              | 291 ms                                                                      | 294 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult  | 3.93 ms                                                                     | 3.98 ms: 1.01x slower                                                       |
| pycparser                | 1.25 sec                                                                    | 1.27 sec: 1.01x slower                                                      |
| coverage                 | 84.1 ms                                                                     | 85.2 ms: 1.01x slower                                                       |
| mdp                      | 2.56 sec                                                                    | 2.60 sec: 1.01x slower                                                      |
| tornado_http             | 121 ms                                                                      | 123 ms: 1.01x slower                                                        |
| deepcopy                 | 304 us                                                                      | 308 us: 1.01x slower                                                        |
| bpe_tokeniser            | 5.16 sec                                                                    | 5.23 sec: 1.01x slower                                                      |
| nbody                    | 83.4 ms                                                                     | 84.7 ms: 1.02x slower                                                       |
| nqueens                  | 94.6 ms                                                                     | 96.1 ms: 1.02x slower                                                       |
| typing_runtime_protocols | 183 us                                                                      | 186 us: 1.02x slower                                                        |
| genshi_xml               | 63.9 ms                                                                     | 64.9 ms: 1.02x slower                                                       |
| dask                     | 398 ms                                                                      | 404 ms: 1.02x slower                                                        |
| tomli_loads              | 2.11 sec                                                                    | 2.15 sec: 1.02x slower                                                      |
| html5lib                 | 72.5 ms                                                                     | 73.9 ms: 1.02x slower                                                       |
| json                     | 5.40 ms                                                                     | 5.51 ms: 1.02x slower                                                       |
| unpickle_pure_python     | 217 us                                                                      | 222 us: 1.02x slower                                                        |
| fannkuch                 | 334 ms                                                                      | 342 ms: 1.02x slower                                                        |
| sqlglot_normalize        | 129 ms                                                                      | 132 ms: 1.03x slower                                                        |
| logging_simple           | 6.22 us                                                                     | 6.38 us: 1.03x slower                                                       |
| raytrace                 | 284 ms                                                                      | 296 ms: 1.04x slower                                                        |
| logging_format           | 6.79 us                                                                     | 7.09 us: 1.04x slower                                                       |
| scimark_sor              | 121 ms                                                                      | 127 ms: 1.05x slower                                                        |
| scimark_lu               | 114 ms                                                                      | 122 ms: 1.07x slower                                                        |
| bench_thread_pool        | 916 us                                                                      | 983 us: 1.07x slower                                                        |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (36): bench_mp_pool, async_tree_none_tg, unpickle_list, async_tree_io_tg, asyncio_websockets, create_gc_cycles, json_dumps, sqlglot_parse, asyncio_tcp, xml_etree_parse, spectral_norm, pickle, async_tree_memoization_tg, regex_effbot, python_startup, asyncio_tcp_ssl, xml_etree_generate, pickle_pure_python, crypto_pyaes, python_startup_no_site, richards_super, async_tree_none, sympy_sum, regex_compile, sympy_integrate, async_tree_cpu_io_mixed_tg, json_loads, pprint_pformat, deepcopy_reduce, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization, deltablue, genshi_text, pprint_safe_repr, pylint

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x