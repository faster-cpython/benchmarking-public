# Results vs. base

- fork: python
- ref: 3f2cfd0462e13368092a
- machine: windows-amd64
- commit hash: 3f2cfd0
- commit date: 2025-01-25
- overall geometric mean: 1.052x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                                                               | 1.76 sec: 1.05x slower                                                                                                     |
| html5lib       | 39.5 ms                                                                                                                | 40.4 ms: 1.02x slower                                                                                                      |
| sphinx         | 659 ms                                                                                                                 | 686 ms: 1.04x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 435 ms                                                                                                                 | 412 ms: 1.05x faster                                                                                                       |
| async_tree_none_tg         | 185 ms                                                                                                                 | 177 ms: 1.05x faster                                                                                                       |
| async_tree_none            | 199 ms                                                                                                                 | 190 ms: 1.05x faster                                                                                                       |
| async_tree_cpu_io_mixed    | 356 ms                                                                                                                 | 345 ms: 1.03x faster                                                                                                       |
| async_tree_memoization     | 233 ms                                                                                                                 | 226 ms: 1.03x faster                                                                                                       |
| async_tree_memoization_tg  | 224 ms                                                                                                                 | 218 ms: 1.03x faster                                                                                                       |
| coroutines                 | 14.8 ms                                                                                                                | 14.5 ms: 1.02x faster                                                                                                      |
| async_tree_io              | 434 ms                                                                                                                 | 426 ms: 1.02x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 353 ms                                                                                                                 | 348 ms: 1.01x faster                                                                                                       |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                               | 1.43 sec: 1.01x slower                                                                                                     |
| asyncio_websockets         | 307 ms                                                                                                                 | 312 ms: 1.02x slower                                                                                                       |
| async_generators           | 227 ms                                                                                                                 | 248 ms: 1.09x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 77.7 ms                                                                                                                | 55.9 ms: 1.39x faster                                                                                                      |
| float          | 51.8 ms                                                                                                                | 40.4 ms: 1.28x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 146 ms: 1.01x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.21x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                                                                 | 114 ms: 1.08x faster                                                                                                       |
| regex_compile  | 89.2 ms                                                                                                                | 84.6 ms: 1.05x faster                                                                                                      |
| regex_v8       | 15.8 ms                                                                                                                | 15.1 ms: 1.05x faster                                                                                                      |
| regex_effbot   | 1.47 ms                                                                                                                | 1.48 ms: 1.01x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                                                                                 | 112 us: 1.48x faster                                                                                                       |
| tomli_loads          | 1.46 sec                                                                                                               | 1.21 sec: 1.20x faster                                                                                                     |
| xml_etree_generate   | 59.1 ms                                                                                                                | 50.2 ms: 1.18x faster                                                                                                      |
| xml_etree_process    | 41.9 ms                                                                                                                | 36.8 ms: 1.14x faster                                                                                                      |
| pickle_pure_python   | 242 us                                                                                                                 | 213 us: 1.13x faster                                                                                                       |
| json_dumps           | 6.85 ms                                                                                                                | 6.27 ms: 1.09x faster                                                                                                      |
| xml_etree_iterparse  | 65.6 ms                                                                                                                | 60.0 ms: 1.09x faster                                                                                                      |
| pickle               | 8.00 us                                                                                                                | 7.93 us: 1.01x faster                                                                                                      |
| unpickle             | 8.58 us                                                                                                                | 8.86 us: 1.03x slower                                                                                                      |
| json_loads           | 14.9 us                                                                                                                | 16.0 us: 1.07x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.08x faster                                                                                                               |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle_list, pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                                                                                | 24.1 ms: 1.01x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.13 ms                                                                                                                | 5.09 ms: 1.40x faster                                                                                                      |
| django_template | 26.4 ms                                                                                                                | 27.4 ms: 1.04x slower                                                                                                      |
| genshi_text     | 16.7 ms                                                                                                                | 19.5 ms: 1.17x slower                                                                                                      |
| genshi_xml      | 36.2 ms                                                                                                                | 47.3 ms: 1.31x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250125-3.14.0a4+-3f2cfd0/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json | results/bm-20250125-3.14.0a4+-3f2cfd0-JIT/bm-20250125-pythonperf1-amd64-python-3f2cfd0462e13368092a-3.14.0a4+-3f2cfd0.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| scimark_sor                | 94.0 ms                                                                                                                | 63.2 ms: 1.49x faster                                                                                                      |
| unpickle_pure_python       | 165 us                                                                                                                 | 112 us: 1.48x faster                                                                                                       |
| mako                       | 7.13 ms                                                                                                                | 5.09 ms: 1.40x faster                                                                                                      |
| nbody                      | 77.7 ms                                                                                                                | 55.9 ms: 1.39x faster                                                                                                      |
| scimark_fft                | 203 ms                                                                                                                 | 146 ms: 1.39x faster                                                                                                       |
| spectral_norm              | 65.0 ms                                                                                                                | 49.2 ms: 1.32x faster                                                                                                      |
| scimark_sparse_mat_mult    | 2.68 ms                                                                                                                | 2.04 ms: 1.32x faster                                                                                                      |
| scimark_monte_carlo        | 49.7 ms                                                                                                                | 38.3 ms: 1.30x faster                                                                                                      |
| float                      | 51.8 ms                                                                                                                | 40.4 ms: 1.28x faster                                                                                                      |
| deepcopy_memo              | 21.6 us                                                                                                                | 17.1 us: 1.27x faster                                                                                                      |
| scimark_lu                 | 70.3 ms                                                                                                                | 56.9 ms: 1.23x faster                                                                                                      |
| tomli_loads                | 1.46 sec                                                                                                               | 1.21 sec: 1.20x faster                                                                                                     |
| logging_silent             | 71.2 ns                                                                                                                | 59.4 ns: 1.20x faster                                                                                                      |
| crypto_pyaes               | 49.2 ms                                                                                                                | 41.1 ms: 1.20x faster                                                                                                      |
| fannkuch                   | 286 ms                                                                                                                 | 241 ms: 1.19x faster                                                                                                       |
| xml_etree_generate         | 59.1 ms                                                                                                                | 50.2 ms: 1.18x faster                                                                                                      |
| pprint_pformat             | 1.13 sec                                                                                                               | 970 ms: 1.17x faster                                                                                                       |
| bpe_tokeniser              | 3.06 sec                                                                                                               | 2.64 sec: 1.16x faster                                                                                                     |
| pprint_safe_repr           | 563 ms                                                                                                                 | 487 ms: 1.16x faster                                                                                                       |
| pyflate                    | 318 ms                                                                                                                 | 277 ms: 1.15x faster                                                                                                       |
| xml_etree_process          | 41.9 ms                                                                                                                | 36.8 ms: 1.14x faster                                                                                                      |
| pickle_pure_python         | 242 us                                                                                                                 | 213 us: 1.13x faster                                                                                                       |
| telco                      | 4.90 ms                                                                                                                | 4.34 ms: 1.13x faster                                                                                                      |
| json_dumps                 | 6.85 ms                                                                                                                | 6.27 ms: 1.09x faster                                                                                                      |
| xml_etree_iterparse        | 65.6 ms                                                                                                                | 60.0 ms: 1.09x faster                                                                                                      |
| regex_dna                  | 123 ms                                                                                                                 | 114 ms: 1.08x faster                                                                                                       |
| pycparser                  | 785 ms                                                                                                                 | 736 ms: 1.07x faster                                                                                                       |
| comprehensions             | 12.7 us                                                                                                                | 11.9 us: 1.07x faster                                                                                                      |
| sqlglot_parse              | 921 us                                                                                                                 | 869 us: 1.06x faster                                                                                                       |
| k_core                     | 1.71 sec                                                                                                               | 1.62 sec: 1.06x faster                                                                                                     |
| regex_compile              | 89.2 ms                                                                                                                | 84.6 ms: 1.05x faster                                                                                                      |
| async_tree_io_tg           | 435 ms                                                                                                                 | 412 ms: 1.05x faster                                                                                                       |
| nqueens                    | 66.8 ms                                                                                                                | 63.7 ms: 1.05x faster                                                                                                      |
| regex_v8                   | 15.8 ms                                                                                                                | 15.1 ms: 1.05x faster                                                                                                      |
| async_tree_none_tg         | 185 ms                                                                                                                 | 177 ms: 1.05x faster                                                                                                       |
| async_tree_none            | 199 ms                                                                                                                 | 190 ms: 1.05x faster                                                                                                       |
| async_tree_cpu_io_mixed    | 356 ms                                                                                                                 | 345 ms: 1.03x faster                                                                                                       |
| mdp                        | 1.58 sec                                                                                                               | 1.53 sec: 1.03x faster                                                                                                     |
| deepcopy_reduce            | 1.95 us                                                                                                                | 1.89 us: 1.03x faster                                                                                                      |
| async_tree_memoization     | 233 ms                                                                                                                 | 226 ms: 1.03x faster                                                                                                       |
| connected_components       | 319 ms                                                                                                                 | 311 ms: 1.03x faster                                                                                                       |
| sqlite_synth               | 1.62 us                                                                                                                | 1.58 us: 1.03x faster                                                                                                      |
| async_tree_memoization_tg  | 224 ms                                                                                                                 | 218 ms: 1.03x faster                                                                                                       |
| chaos                      | 43.1 ms                                                                                                                | 42.0 ms: 1.03x faster                                                                                                      |
| sqlglot_transpile          | 1.14 ms                                                                                                                | 1.11 ms: 1.02x faster                                                                                                      |
| coroutines                 | 14.8 ms                                                                                                                | 14.5 ms: 1.02x faster                                                                                                      |
| async_tree_io              | 434 ms                                                                                                                 | 426 ms: 1.02x faster                                                                                                       |
| shortest_path              | 354 ms                                                                                                                 | 347 ms: 1.02x faster                                                                                                       |
| sympy_integrate            | 13.8 ms                                                                                                                | 13.6 ms: 1.02x faster                                                                                                      |
| coverage                   | 48.5 ms                                                                                                                | 47.7 ms: 1.02x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 353 ms                                                                                                                 | 348 ms: 1.01x faster                                                                                                       |
| python_startup             | 24.3 ms                                                                                                                | 24.1 ms: 1.01x faster                                                                                                      |
| meteor_contest             | 77.6 ms                                                                                                                | 76.8 ms: 1.01x faster                                                                                                      |
| deepcopy                   | 189 us                                                                                                                 | 188 us: 1.01x faster                                                                                                       |
| pickle                     | 8.00 us                                                                                                                | 7.93 us: 1.01x faster                                                                                                      |
| pidigits                   | 147 ms                                                                                                                 | 146 ms: 1.01x faster                                                                                                       |
| logging_simple             | 6.45 us                                                                                                                | 6.48 us: 1.00x slower                                                                                                      |
| regex_effbot               | 1.47 ms                                                                                                                | 1.48 ms: 1.01x slower                                                                                                      |
| logging_format             | 6.87 us                                                                                                                | 6.92 us: 1.01x slower                                                                                                      |
| bench_mp_pool              | 87.7 ms                                                                                                                | 88.4 ms: 1.01x slower                                                                                                      |
| asyncio_tcp_ssl            | 1.42 sec                                                                                                               | 1.43 sec: 1.01x slower                                                                                                     |
| sympy_expand               | 308 ms                                                                                                                 | 311 ms: 1.01x slower                                                                                                       |
| pathlib                    | 77.7 ms                                                                                                                | 78.5 ms: 1.01x slower                                                                                                      |
| sympy_str                  | 180 ms                                                                                                                 | 182 ms: 1.01x slower                                                                                                       |
| typing_runtime_protocols   | 111 us                                                                                                                 | 112 us: 1.01x slower                                                                                                       |
| dulwich_log                | 42.6 ms                                                                                                                | 43.1 ms: 1.01x slower                                                                                                      |
| asyncio_websockets         | 307 ms                                                                                                                 | 312 ms: 1.02x slower                                                                                                       |
| go                         | 93.4 ms                                                                                                                | 95.4 ms: 1.02x slower                                                                                                      |
| sympy_sum                  | 91.0 ms                                                                                                                | 93.1 ms: 1.02x slower                                                                                                      |
| html5lib                   | 39.5 ms                                                                                                                | 40.4 ms: 1.02x slower                                                                                                      |
| sqlglot_normalize          | 201 ms                                                                                                                 | 208 ms: 1.03x slower                                                                                                       |
| unpickle                   | 8.58 us                                                                                                                | 8.86 us: 1.03x slower                                                                                                      |
| django_template            | 26.4 ms                                                                                                                | 27.4 ms: 1.04x slower                                                                                                      |
| sphinx                     | 659 ms                                                                                                                 | 686 ms: 1.04x slower                                                                                                       |
| thrift                     | 520 us                                                                                                                 | 544 us: 1.04x slower                                                                                                       |
| sqlglot_optimize           | 36.8 ms                                                                                                                | 38.5 ms: 1.05x slower                                                                                                      |
| docutils                   | 1.69 sec                                                                                                               | 1.76 sec: 1.05x slower                                                                                                     |
| many_optionals             | 433 us                                                                                                                 | 456 us: 1.05x slower                                                                                                       |
| pylint                     | 201 ms                                                                                                                 | 212 ms: 1.06x slower                                                                                                       |
| hexiom                     | 4.76 ms                                                                                                                | 5.05 ms: 1.06x slower                                                                                                      |
| json_loads                 | 14.9 us                                                                                                                | 16.0 us: 1.07x slower                                                                                                      |
| richards_super             | 37.2 ms                                                                                                                | 40.6 ms: 1.09x slower                                                                                                      |
| async_generators           | 227 ms                                                                                                                 | 248 ms: 1.09x slower                                                                                                       |
| richards                   | 32.7 ms                                                                                                                | 35.9 ms: 1.10x slower                                                                                                      |
| raytrace                   | 207 ms                                                                                                                 | 228 ms: 1.10x slower                                                                                                       |
| generators                 | 22.0 ms                                                                                                                | 25.0 ms: 1.14x slower                                                                                                      |
| genshi_text                | 16.7 ms                                                                                                                | 19.5 ms: 1.17x slower                                                                                                      |
| genshi_xml                 | 36.2 ms                                                                                                                | 47.3 ms: 1.31x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (14): subparsers, python_startup_no_site, xml_etree_parse, unpickle_list, 2to3, gc_traversal, json, create_gc_cycles, pickle_dict, pickle_list, deltablue, asyncio_tcp, bench_thread_pool, unpack_sequence

- Geometric mean (including insignificant results): 1.052x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown