# Results vs. 3.13.0b2

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: darwin-arm64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.04x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.10x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.3 ms: 1.04x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 81.7 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                      | 1.11x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 201 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.1 ms: 1.06x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.1 ms: 1.05x faster                                                 |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 75.6 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 34.3 ms: 1.08x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.08x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                 |
| json_dumps           | 6.23 ms                                                    | 6.17 ms: 1.01x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.89 us: 1.00x slower                                                 |
| pickle_list          | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| pickle_dict          | 18.3 us                                                    | 18.5 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (5): pickle, pickle_pure_python, json_loads, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.9 ms: 1.11x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                 |
| django_template | 19.4 ms                                                    | 22.8 ms: 1.18x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 41.3 ms: 1.38x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.0 us: 1.41x faster                                                 |
| deepcopy                         | 204 us                                                     | 152 us: 1.34x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 678 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 705 ms: 1.09x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 87.3 ms: 1.09x faster                                                 |
| xml_etree_process                | 37.1 ms                                                    | 34.3 ms: 1.08x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.06x faster                                                |
| float                            | 48.6 ms                                                    | 46.1 ms: 1.05x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 188 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 63.9 ms: 1.05x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 201 ms: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 51.1 ms: 1.03x faster                                                 |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                  |
| coverage                         | 45.0 ms                                                    | 44.4 ms: 1.01x faster                                                 |
| json                             | 2.93 ms                                                    | 2.90 ms: 1.01x faster                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.17 ms: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.89 us: 1.00x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 66.7 ms: 1.00x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                 |
| pickle_list                      | 2.96 us                                                    | 2.98 us: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                                |
| create_gc_cycles                 | 897 us                                                     | 905 us: 1.01x slower                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.5 us: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| sqlite_synth                     | 1.55 us                                                    | 1.58 us: 1.02x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.28 us: 1.02x slower                                                 |
| pyflate                          | 321 ms                                                     | 327 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                  |
| html5lib                         | 31.2 ms                                                    | 32.3 ms: 1.04x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.4 ms: 1.04x slower                                                 |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.78 ms: 1.04x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 62.5 ns: 1.04x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 470 us: 1.05x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.0 ms: 1.05x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.1 ms: 1.06x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 74.9 ms: 1.07x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.4 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.96 ms: 1.07x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 93.6 us: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| pycparser                        | 632 ms                                                     | 685 ms: 1.08x slower                                                  |
| fannkuch                         | 248 ms                                                     | 269 ms: 1.08x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 180 ms: 1.08x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 504 ms: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.56 sec: 1.09x slower                                                |
| pprint_pformat                   | 947 ms                                                     | 1.03 sec: 1.09x slower                                                |
| bench_mp_pool                    | 47.2 ms                                                    | 51.6 ms: 1.09x slower                                                 |
| sympy_str                        | 131 ms                                                     | 144 ms: 1.09x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 75.8 ms: 1.09x slower                                                 |
| 2to3                             | 161 ms                                                     | 176 ms: 1.10x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 248 ms: 1.10x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.36 ms: 1.10x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 75.6 ms: 1.10x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 57.9 ms: 1.11x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.9 ms: 1.11x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 11.6 ms: 1.12x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.0 ms: 1.13x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.3 ms: 1.14x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.73 ms: 1.17x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.17x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 855 us: 1.17x slower                                                  |
| chaos                            | 34.0 ms                                                    | 39.9 ms: 1.17x slower                                                 |
| raytrace                         | 147 ms                                                     | 173 ms: 1.17x slower                                                  |
| django_template                  | 19.4 ms                                                    | 22.8 ms: 1.18x slower                                                 |
| pylint                           | 170 ms                                                     | 205 ms: 1.21x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 81.7 ms: 1.23x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 12.7 us: 1.25x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 47.9 ms: 1.36x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 41.3 ms: 1.38x slower                                                 |
| richards                         | 31.8 ms                                                    | 45.9 ms: 1.44x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (15): async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_websockets, go, pickle, pickle_pure_python, logging_format, pidigits, json_loads, xml_etree_iterparse, xml_etree_parse, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.61x