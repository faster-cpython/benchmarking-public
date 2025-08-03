# Results vs. base

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.100x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 225 ms                                                                                                               | 232 ms: 1.03x slower                                                                                                       |
| docutils       | 1.64 sec                                                                                                             | 2.97 sec: 1.81x slower                                                                                                     |
| sphinx         | 645 ms                                                                                                               | 731 ms: 1.13x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                | 1.21x slower                                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 406 ms                                                                                                               | 335 ms: 1.21x faster                                                                                                       |
| asyncio_websockets         | 168 ms                                                                                                               | 141 ms: 1.19x faster                                                                                                       |
| async_tree_io              | 405 ms                                                                                                               | 352 ms: 1.15x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 356 ms                                                                                                               | 316 ms: 1.13x faster                                                                                                       |
| async_tree_none_tg         | 173 ms                                                                                                               | 155 ms: 1.12x faster                                                                                                       |
| async_tree_memoization_tg  | 219 ms                                                                                                               | 203 ms: 1.08x faster                                                                                                       |
| async_tree_none            | 188 ms                                                                                                               | 178 ms: 1.06x faster                                                                                                       |
| async_tree_memoization     | 215 ms                                                                                                               | 224 ms: 1.04x slower                                                                                                       |
| coroutines                 | 14.4 ms                                                                                                              | 15.1 ms: 1.05x slower                                                                                                      |
| async_generators           | 239 ms                                                                                                               | 263 ms: 1.10x slower                                                                                                       |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                             | 2.34 sec: 1.64x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.02x faster                                                                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                                                                               | 142 ms: 1.04x faster                                                                                                       |
| nbody          | 67.0 ms                                                                                                              | 82.2 ms: 1.23x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                | 1.06x slower                                                                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                                                               | 112 ms: 1.06x faster                                                                                                       |
| regex_v8       | 13.9 ms                                                                                                              | 13.1 ms: 1.06x faster                                                                                                      |
| regex_compile  | 81.2 ms                                                                                                              | 94.4 ms: 1.16x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 68.0 ms                                                                                                              | 59.5 ms: 1.14x faster                                                                                                      |
| xml_etree_parse      | 92.4 ms                                                                                                              | 90.6 ms: 1.02x faster                                                                                                      |
| pickle_list          | 3.28 us                                                                                                              | 3.23 us: 1.02x faster                                                                                                      |
| unpickle_list        | 3.03 us                                                                                                              | 3.10 us: 1.03x slower                                                                                                      |
| pickle_dict          | 20.2 us                                                                                                              | 21.2 us: 1.05x slower                                                                                                      |
| pickle               | 7.90 us                                                                                                              | 8.47 us: 1.07x slower                                                                                                      |
| xml_etree_generate   | 58.6 ms                                                                                                              | 63.1 ms: 1.08x slower                                                                                                      |
| json_dumps           | 6.21 ms                                                                                                              | 6.72 ms: 1.08x slower                                                                                                      |
| pickle_pure_python   | 223 us                                                                                                               | 242 us: 1.08x slower                                                                                                       |
| xml_etree_process    | 40.7 ms                                                                                                              | 44.2 ms: 1.09x slower                                                                                                      |
| unpickle_pure_python | 144 us                                                                                                               | 157 us: 1.09x slower                                                                                                       |
| json_loads           | 14.4 us                                                                                                              | 15.8 us: 1.10x slower                                                                                                      |
| unpickle             | 8.67 us                                                                                                              | 10.6 us: 1.23x slower                                                                                                      |
| tomli_loads          | 1.43 sec                                                                                                             | 2.77 sec: 1.93x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                | 1.10x slower                                                                                                               |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| django_template | 24.6 ms                                                                                                              | 27.3 ms: 1.11x slower                                                                                                      |
| genshi_xml      | 36.2 ms                                                                                                              | 40.3 ms: 1.11x slower                                                                                                      |
| genshi_text     | 15.9 ms                                                                                                              | 19.7 ms: 1.24x slower                                                                                                      |
| mako            | 6.67 ms                                                                                                              | 9.71 ms: 1.46x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                | 1.22x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json | results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 2.17 ms                                                                                                              | 1.22 ms: 1.77x faster                                                                                                      |
| create_gc_cycles           | 1.39 ms                                                                                                              | 1.05 ms: 1.33x faster                                                                                                      |
| async_tree_io_tg           | 406 ms                                                                                                               | 335 ms: 1.21x faster                                                                                                       |
| asyncio_websockets         | 168 ms                                                                                                               | 141 ms: 1.19x faster                                                                                                       |
| bench_mp_pool              | 96.1 ms                                                                                                              | 80.7 ms: 1.19x faster                                                                                                      |
| sqlite_synth               | 1.59 us                                                                                                              | 1.36 us: 1.17x faster                                                                                                      |
| async_tree_io              | 405 ms                                                                                                               | 352 ms: 1.15x faster                                                                                                       |
| xml_etree_iterparse        | 68.0 ms                                                                                                              | 59.5 ms: 1.14x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 356 ms                                                                                                               | 316 ms: 1.13x faster                                                                                                       |
| async_tree_none_tg         | 173 ms                                                                                                               | 155 ms: 1.12x faster                                                                                                       |
| async_tree_memoization_tg  | 219 ms                                                                                                               | 203 ms: 1.08x faster                                                                                                       |
| regex_dna                  | 119 ms                                                                                                               | 112 ms: 1.06x faster                                                                                                       |
| regex_v8                   | 13.9 ms                                                                                                              | 13.1 ms: 1.06x faster                                                                                                      |
| async_tree_none            | 188 ms                                                                                                               | 178 ms: 1.06x faster                                                                                                       |
| pidigits                   | 148 ms                                                                                                               | 142 ms: 1.04x faster                                                                                                       |
| dulwich_log                | 44.2 ms                                                                                                              | 42.9 ms: 1.03x faster                                                                                                      |
| xml_etree_parse            | 92.4 ms                                                                                                              | 90.6 ms: 1.02x faster                                                                                                      |
| pickle_list                | 3.28 us                                                                                                              | 3.23 us: 1.02x faster                                                                                                      |
| json                       | 3.07 ms                                                                                                              | 3.15 ms: 1.02x slower                                                                                                      |
| unpickle_list              | 3.03 us                                                                                                              | 3.10 us: 1.03x slower                                                                                                      |
| 2to3                       | 225 ms                                                                                                               | 232 ms: 1.03x slower                                                                                                       |
| async_tree_memoization     | 215 ms                                                                                                               | 224 ms: 1.04x slower                                                                                                       |
| coroutines                 | 14.4 ms                                                                                                              | 15.1 ms: 1.05x slower                                                                                                      |
| pickle_dict                | 20.2 us                                                                                                              | 21.2 us: 1.05x slower                                                                                                      |
| fannkuch                   | 277 ms                                                                                                               | 294 ms: 1.06x slower                                                                                                       |
| pickle                     | 7.90 us                                                                                                              | 8.47 us: 1.07x slower                                                                                                      |
| sympy_expand               | 300 ms                                                                                                               | 322 ms: 1.07x slower                                                                                                       |
| xml_etree_generate         | 58.6 ms                                                                                                              | 63.1 ms: 1.08x slower                                                                                                      |
| json_dumps                 | 6.21 ms                                                                                                              | 6.72 ms: 1.08x slower                                                                                                      |
| sqlglot_v2_optimize        | 34.7 ms                                                                                                              | 37.5 ms: 1.08x slower                                                                                                      |
| pickle_pure_python         | 223 us                                                                                                               | 242 us: 1.08x slower                                                                                                       |
| sqlglot_v2_normalize       | 72.2 ms                                                                                                              | 78.3 ms: 1.08x slower                                                                                                      |
| pyflate                    | 302 ms                                                                                                               | 328 ms: 1.08x slower                                                                                                       |
| xml_etree_process          | 40.7 ms                                                                                                              | 44.2 ms: 1.09x slower                                                                                                      |
| logging_simple             | 6.17 us                                                                                                              | 6.72 us: 1.09x slower                                                                                                      |
| unpickle_pure_python       | 144 us                                                                                                               | 157 us: 1.09x slower                                                                                                       |
| logging_format             | 6.62 us                                                                                                              | 7.23 us: 1.09x slower                                                                                                      |
| scimark_lu                 | 62.2 ms                                                                                                              | 68.2 ms: 1.10x slower                                                                                                      |
| logging_silent             | 56.6 ns                                                                                                              | 62.1 ns: 1.10x slower                                                                                                      |
| json_loads                 | 14.4 us                                                                                                              | 15.8 us: 1.10x slower                                                                                                      |
| async_generators           | 239 ms                                                                                                               | 263 ms: 1.10x slower                                                                                                       |
| hexiom                     | 4.25 ms                                                                                                              | 4.67 ms: 1.10x slower                                                                                                      |
| django_template            | 24.6 ms                                                                                                              | 27.3 ms: 1.11x slower                                                                                                      |
| genshi_xml                 | 36.2 ms                                                                                                              | 40.3 ms: 1.11x slower                                                                                                      |
| deltablue                  | 2.22 ms                                                                                                              | 2.48 ms: 1.12x slower                                                                                                      |
| comprehensions             | 11.2 us                                                                                                              | 12.5 us: 1.12x slower                                                                                                      |
| chaos                      | 42.0 ms                                                                                                              | 46.9 ms: 1.12x slower                                                                                                      |
| pprint_safe_repr           | 507 ms                                                                                                               | 567 ms: 1.12x slower                                                                                                       |
| many_optionals             | 585 us                                                                                                               | 656 us: 1.12x slower                                                                                                       |
| sympy_integrate            | 12.6 ms                                                                                                              | 14.2 ms: 1.12x slower                                                                                                      |
| spectral_norm              | 65.9 ms                                                                                                              | 74.2 ms: 1.13x slower                                                                                                      |
| scimark_sor                | 79.3 ms                                                                                                              | 89.8 ms: 1.13x slower                                                                                                      |
| sympy_str                  | 171 ms                                                                                                               | 193 ms: 1.13x slower                                                                                                       |
| sphinx                     | 645 ms                                                                                                               | 731 ms: 1.13x slower                                                                                                       |
| deepcopy_reduce            | 1.87 us                                                                                                              | 2.13 us: 1.14x slower                                                                                                      |
| thrift                     | 503 us                                                                                                               | 577 us: 1.15x slower                                                                                                       |
| sympy_sum                  | 88.9 ms                                                                                                              | 102 ms: 1.15x slower                                                                                                       |
| go                         | 80.7 ms                                                                                                              | 92.9 ms: 1.15x slower                                                                                                      |
| telco                      | 4.64 ms                                                                                                              | 5.34 ms: 1.15x slower                                                                                                      |
| sqlglot_v2_transpile       | 1.05 ms                                                                                                              | 1.22 ms: 1.16x slower                                                                                                      |
| deepcopy_memo              | 18.1 us                                                                                                              | 20.9 us: 1.16x slower                                                                                                      |
| sqlglot_v2_parse           | 856 us                                                                                                               | 991 us: 1.16x slower                                                                                                       |
| subparsers                 | 31.4 ms                                                                                                              | 36.4 ms: 1.16x slower                                                                                                      |
| unpack_sequence            | 33.7 ns                                                                                                              | 39.1 ns: 1.16x slower                                                                                                      |
| generators                 | 20.0 ms                                                                                                              | 23.2 ms: 1.16x slower                                                                                                      |
| crypto_pyaes               | 48.9 ms                                                                                                              | 56.8 ms: 1.16x slower                                                                                                      |
| regex_compile              | 81.2 ms                                                                                                              | 94.4 ms: 1.16x slower                                                                                                      |
| nqueens                    | 63.7 ms                                                                                                              | 74.6 ms: 1.17x slower                                                                                                      |
| deepcopy                   | 172 us                                                                                                               | 203 us: 1.18x slower                                                                                                       |
| raytrace                   | 179 ms                                                                                                               | 211 ms: 1.18x slower                                                                                                       |
| scimark_fft                | 191 ms                                                                                                               | 227 ms: 1.19x slower                                                                                                       |
| meteor_contest             | 74.7 ms                                                                                                              | 89.1 ms: 1.19x slower                                                                                                      |
| scimark_sparse_mat_mult    | 2.68 ms                                                                                                              | 3.20 ms: 1.19x slower                                                                                                      |
| nbody                      | 67.0 ms                                                                                                              | 82.2 ms: 1.23x slower                                                                                                      |
| unpickle                   | 8.67 us                                                                                                              | 10.6 us: 1.23x slower                                                                                                      |
| genshi_text                | 15.9 ms                                                                                                              | 19.7 ms: 1.24x slower                                                                                                      |
| typing_runtime_protocols   | 105 us                                                                                                               | 130 us: 1.24x slower                                                                                                       |
| richards                   | 28.6 ms                                                                                                              | 35.5 ms: 1.24x slower                                                                                                      |
| scimark_monte_carlo        | 41.2 ms                                                                                                              | 51.5 ms: 1.25x slower                                                                                                      |
| richards_super             | 33.0 ms                                                                                                              | 41.3 ms: 1.25x slower                                                                                                      |
| bench_thread_pool          | 872 us                                                                                                               | 1.10 ms: 1.26x slower                                                                                                      |
| coverage                   | 49.9 ms                                                                                                              | 66.3 ms: 1.33x slower                                                                                                      |
| mdp                        | 834 ms                                                                                                               | 1.18 sec: 1.42x slower                                                                                                     |
| mako                       | 6.67 ms                                                                                                              | 9.71 ms: 1.46x slower                                                                                                      |
| k_core                     | 1.72 sec                                                                                                             | 2.72 sec: 1.58x slower                                                                                                     |
| pprint_pformat             | 1.05 sec                                                                                                             | 1.72 sec: 1.64x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                             | 2.34 sec: 1.64x slower                                                                                                     |
| docutils                   | 1.64 sec                                                                                                             | 2.97 sec: 1.81x slower                                                                                                     |
| shortest_path              | 367 ms                                                                                                               | 673 ms: 1.83x slower                                                                                                       |
| bpe_tokeniser              | 2.97 sec                                                                                                             | 5.59 sec: 1.88x slower                                                                                                     |
| connected_components       | 335 ms                                                                                                               | 636 ms: 1.90x slower                                                                                                       |
| tomli_loads                | 1.43 sec                                                                                                             | 2.77 sec: 1.93x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.11x slower                                                                                                               |

Benchmark hidden because not significant (10): asyncio_tcp, async_tree_cpu_io_mixed, python_startup_no_site, regex_effbot, pycparser, python_startup, float, pathlib, html5lib, pylint

- Geometric mean (including insignificant results): 1.100x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown