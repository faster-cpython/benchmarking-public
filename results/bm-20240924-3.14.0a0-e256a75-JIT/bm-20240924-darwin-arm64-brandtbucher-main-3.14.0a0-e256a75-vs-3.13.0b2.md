# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: darwin-arm64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.03x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.53x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 175 ms: 1.09x slower                                        |
| docutils       | 1.44 sec                                                   | 1.55 sec: 1.08x slower                                      |
| html5lib       | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                       |
| tornado_http   | 66.7 ms                                                    | 86.8 ms: 1.30x slower                                       |
| Geometric mean | (ref)                                                      | 1.13x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                        |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                        |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                        |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                        |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                        |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                        |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                       |
| async_tree_io                    | 563 ms                                                     | 589 ms: 1.05x slower                                        |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                        |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.1 ms: 1.05x faster                                       |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                      | 1.00x slower                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                       |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                       |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                        |
| regex_compile  | 68.5 ms                                                    | 75.6 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                      | 1.00x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.18x faster                                      |
| xml_etree_process    | 37.1 ms                                                    | 34.0 ms: 1.09x faster                                       |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                        |
| xml_etree_generate   | 52.7 ms                                                    | 49.7 ms: 1.06x faster                                       |
| pickle               | 7.48 us                                                    | 7.43 us: 1.01x faster                                       |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.00x faster                                       |
| pickle_pure_python   | 179 us                                                     | 178 us: 1.00x faster                                        |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                       |
| unpickle             | 9.12 us                                                    | 9.22 us: 1.01x slower                                       |
| json_dumps           | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                       |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                        |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                |

Benchmark hidden because not significant (3): pickle_dict, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                       |
| python_startup_no_site | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                       |
| Geometric mean         | (ref)                                                      | 1.01x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.48 ms: 1.08x faster                                       |
| django_template | 19.4 ms                                                    | 22.4 ms: 1.15x slower                                       |
| genshi_text     | 13.9 ms                                                    | 17.1 ms: 1.23x slower                                       |
| genshi_xml      | 29.9 ms                                                    | 41.6 ms: 1.39x slower                                       |
| Geometric mean  | (ref)                                                      | 1.16x slower                                                |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.3 us: 1.39x faster                                       |
| deepcopy                         | 204 us                                                     | 155 us: 1.32x faster                                        |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                       |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.18x faster                                      |
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                        |
| async_tree_eager_io_tg           | 768 ms                                                     | 701 ms: 1.09x faster                                        |
| xml_etree_process                | 37.1 ms                                                    | 34.0 ms: 1.09x faster                                       |
| scimark_sor                      | 94.9 ms                                                    | 87.8 ms: 1.08x faster                                       |
| mako                             | 6.99 ms                                                    | 6.48 ms: 1.08x faster                                       |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                        |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                        |
| xml_etree_generate               | 52.7 ms                                                    | 49.7 ms: 1.06x faster                                       |
| float                            | 48.6 ms                                                    | 46.1 ms: 1.05x faster                                       |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                      |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                        |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                        |
| scimark_lu                       | 66.9 ms                                                    | 63.7 ms: 1.05x faster                                       |
| regex_effbot                     | 2.58 ms                                                    | 2.46 ms: 1.05x faster                                       |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                       |
| thrift                           | 435 us                                                     | 423 us: 1.03x faster                                        |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                        |
| logging_simple                   | 3.04 us                                                    | 2.97 us: 1.03x faster                                       |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                        |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                        |
| coverage                         | 45.0 ms                                                    | 44.4 ms: 1.01x faster                                       |
| logging_format                   | 3.31 us                                                    | 3.27 us: 1.01x faster                                       |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                      |
| pickle                           | 7.48 us                                                    | 7.43 us: 1.01x faster                                       |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.00x faster                                       |
| pickle_pure_python               | 179 us                                                     | 178 us: 1.00x faster                                        |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                        |
| gc_traversal                     | 2.45 ms                                                    | 2.45 ms: 1.00x slower                                       |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.06 sec: 1.00x slower                                      |
| create_gc_cycles                 | 897 us                                                     | 902 us: 1.01x slower                                        |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                       |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                       |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                       |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                        |
| unpickle                         | 9.12 us                                                    | 9.22 us: 1.01x slower                                       |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                       |
| python_startup                   | 15.2 ms                                                    | 15.3 ms: 1.01x slower                                       |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                        |
| json_dumps                       | 6.23 ms                                                    | 6.31 ms: 1.01x slower                                       |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                        |
| python_startup_no_site           | 12.3 ms                                                    | 12.5 ms: 1.02x slower                                       |
| pyflate                          | 321 ms                                                     | 328 ms: 1.02x slower                                        |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                       |
| telco                            | 4.60 ms                                                    | 4.72 ms: 1.02x slower                                       |
| go                               | 101 ms                                                     | 103 ms: 1.03x slower                                        |
| logging_silent                   | 60.1 ns                                                    | 62.0 ns: 1.03x slower                                       |
| scimark_fft                      | 181 ms                                                     | 186 ms: 1.03x slower                                        |
| pathlib                          | 23.3 ms                                                    | 24.2 ms: 1.04x slower                                       |
| async_generators                 | 281 ms                                                     | 293 ms: 1.04x slower                                        |
| async_tree_io                    | 563 ms                                                     | 589 ms: 1.05x slower                                        |
| html5lib                         | 31.2 ms                                                    | 32.6 ms: 1.05x slower                                       |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                       |
| crypto_pyaes                     | 49.5 ms                                                    | 52.1 ms: 1.05x slower                                       |
| bench_thread_pool                | 447 us                                                     | 471 us: 1.05x slower                                        |
| async_tree_eager                 | 60.3 ms                                                    | 63.8 ms: 1.06x slower                                       |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                       |
| pprint_safe_repr                 | 465 ms                                                     | 495 ms: 1.07x slower                                        |
| fannkuch                         | 248 ms                                                     | 265 ms: 1.07x slower                                        |
| generators                       | 22.9 ms                                                    | 24.4 ms: 1.07x slower                                       |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                        |
| meteor_contest                   | 70.3 ms                                                    | 75.3 ms: 1.07x slower                                       |
| pprint_pformat                   | 947 ms                                                     | 1.01 sec: 1.07x slower                                      |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.98 ms: 1.07x slower                                       |
| pycparser                        | 632 ms                                                     | 680 ms: 1.08x slower                                        |
| bench_mp_pool                    | 47.2 ms                                                    | 50.9 ms: 1.08x slower                                       |
| docutils                         | 1.44 sec                                                   | 1.55 sec: 1.08x slower                                      |
| typing_runtime_protocols         | 87.6 us                                                    | 95.2 us: 1.09x slower                                       |
| sympy_sum                        | 69.2 ms                                                    | 75.4 ms: 1.09x slower                                       |
| 2to3                             | 161 ms                                                     | 175 ms: 1.09x slower                                        |
| sympy_str                        | 131 ms                                                     | 144 ms: 1.09x slower                                        |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.09x slower                                        |
| sqlglot_normalize                | 166 ms                                                     | 181 ms: 1.10x slower                                        |
| deltablue                        | 2.14 ms                                                    | 2.35 ms: 1.10x slower                                       |
| regex_compile                    | 68.5 ms                                                    | 75.6 ms: 1.10x slower                                       |
| nqueens                          | 52.2 ms                                                    | 57.7 ms: 1.10x slower                                       |
| sympy_integrate                  | 10.3 ms                                                    | 11.5 ms: 1.12x slower                                       |
| scimark_monte_carlo              | 42.5 ms                                                    | 47.9 ms: 1.13x slower                                       |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.5 ms: 1.15x slower                                       |
| django_template                  | 19.4 ms                                                    | 22.4 ms: 1.15x slower                                       |
| sqlglot_parse                    | 732 us                                                     | 850 us: 1.16x slower                                        |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.17x slower                                       |
| hexiom                           | 4.06 ms                                                    | 4.76 ms: 1.17x slower                                       |
| chaos                            | 34.0 ms                                                    | 40.0 ms: 1.18x slower                                       |
| raytrace                         | 147 ms                                                     | 173 ms: 1.18x slower                                        |
| pylint                           | 170 ms                                                     | 206 ms: 1.21x slower                                        |
| genshi_text                      | 13.9 ms                                                    | 17.1 ms: 1.23x slower                                       |
| comprehensions                   | 10.2 us                                                    | 12.7 us: 1.25x slower                                       |
| tornado_http                     | 66.7 ms                                                    | 86.8 ms: 1.30x slower                                       |
| richards_super                   | 35.2 ms                                                    | 47.6 ms: 1.35x slower                                       |
| genshi_xml                       | 29.9 ms                                                    | 41.6 ms: 1.39x slower                                       |
| richards                         | 31.8 ms                                                    | 44.4 ms: 1.40x slower                                       |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                |

Benchmark hidden because not significant (9): async_tree_io_tg, asyncio_tcp, pickle_dict, pidigits, json_loads, xml_etree_iterparse, json, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-darwin-arm64-brandtbucher-main-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.53x