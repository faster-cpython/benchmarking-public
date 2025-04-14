# Results vs. base

- fork: python
- ref: 359c7dde3bb074e02968
- machine: windows-amd64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.031x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                                                                 | 219 ms: 1.02x faster                                                                                                       |
| docutils       | 1.65 sec                                                                                                               | 1.69 sec: 1.03x slower                                                                                                     |
| sphinx         | 640 ms                                                                                                                 | 647 ms: 1.01x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp                | 521 ms                                                                                                                 | 416 ms: 1.25x faster                                                                                                       |
| asyncio_tcp_ssl            | 1.44 sec                                                                                                               | 1.31 sec: 1.10x faster                                                                                                     |
| async_tree_io_tg           | 421 ms                                                                                                                 | 413 ms: 1.02x faster                                                                                                       |
| async_tree_none            | 190 ms                                                                                                                 | 186 ms: 1.02x faster                                                                                                       |
| asyncio_websockets         | 314 ms                                                                                                                 | 308 ms: 1.02x faster                                                                                                       |
| async_tree_memoization_tg  | 221 ms                                                                                                                 | 218 ms: 1.02x faster                                                                                                       |
| async_tree_none_tg         | 179 ms                                                                                                                 | 177 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| async_tree_cpu_io_mixed    | 343 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| coroutines                 | 13.6 ms                                                                                                                | 13.9 ms: 1.02x slower                                                                                                      |
| async_generators           | 222 ms                                                                                                                 | 234 ms: 1.05x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 68.9 ms                                                                                                                | 59.8 ms: 1.15x faster                                                                                                      |
| float          | 46.8 ms                                                                                                                | 44.8 ms: 1.04x faster                                                                                                      |
| pidigits       | 150 ms                                                                                                                 | 150 ms: 1.00x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 86.0 ms                                                                                                                | 82.7 ms: 1.04x faster                                                                                                      |
| regex_v8       | 14.3 ms                                                                                                                | 14.5 ms: 1.01x slower                                                                                                      |
| regex_effbot   | 1.42 ms                                                                                                                | 1.45 ms: 1.02x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 149 us                                                                                                                 | 118 us: 1.26x faster                                                                                                       |
| tomli_loads          | 1.45 sec                                                                                                               | 1.21 sec: 1.20x faster                                                                                                     |
| xml_etree_generate   | 56.8 ms                                                                                                                | 51.5 ms: 1.10x faster                                                                                                      |
| xml_etree_process    | 40.0 ms                                                                                                                | 37.0 ms: 1.08x faster                                                                                                      |
| pickle_pure_python   | 224 us                                                                                                                 | 209 us: 1.07x faster                                                                                                       |
| json_loads           | 15.7 us                                                                                                                | 14.8 us: 1.06x faster                                                                                                      |
| unpickle             | 8.95 us                                                                                                                | 8.57 us: 1.05x faster                                                                                                      |
| unpickle_list        | 2.76 us                                                                                                                | 2.65 us: 1.04x faster                                                                                                      |
| xml_etree_iterparse  | 63.1 ms                                                                                                                | 61.1 ms: 1.03x faster                                                                                                      |
| json_dumps           | 6.68 ms                                                                                                                | 6.55 ms: 1.02x faster                                                                                                      |
| pickle_list          | 2.95 us                                                                                                                | 2.97 us: 1.01x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.06x faster                                                                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.89 ms                                                                                                                | 5.34 ms: 1.29x faster                                                                                                      |
| genshi_text     | 16.3 ms                                                                                                                | 16.8 ms: 1.03x slower                                                                                                      |
| django_template | 24.9 ms                                                                                                                | 26.0 ms: 1.04x slower                                                                                                      |
| genshi_xml      | 35.3 ms                                                                                                                | 39.1 ms: 1.11x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.02x faster                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-pythonperf1-amd64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako                       | 6.89 ms                                                                                                                | 5.34 ms: 1.29x faster                                                                                                      |
| unpickle_pure_python       | 149 us                                                                                                                 | 118 us: 1.26x faster                                                                                                       |
| asyncio_tcp                | 521 ms                                                                                                                 | 416 ms: 1.25x faster                                                                                                       |
| scimark_fft                | 190 ms                                                                                                                 | 153 ms: 1.24x faster                                                                                                       |
| scimark_sparse_mat_mult    | 2.68 ms                                                                                                                | 2.17 ms: 1.23x faster                                                                                                      |
| fannkuch                   | 276 ms                                                                                                                 | 230 ms: 1.20x faster                                                                                                       |
| tomli_loads                | 1.45 sec                                                                                                               | 1.21 sec: 1.20x faster                                                                                                     |
| nbody                      | 68.9 ms                                                                                                                | 59.8 ms: 1.15x faster                                                                                                      |
| pyflate                    | 309 ms                                                                                                                 | 271 ms: 1.14x faster                                                                                                       |
| bpe_tokeniser              | 2.92 sec                                                                                                               | 2.61 sec: 1.12x faster                                                                                                     |
| xml_etree_generate         | 56.8 ms                                                                                                                | 51.5 ms: 1.10x faster                                                                                                      |
| asyncio_tcp_ssl            | 1.44 sec                                                                                                               | 1.31 sec: 1.10x faster                                                                                                     |
| deepcopy_memo              | 20.6 us                                                                                                                | 19.0 us: 1.09x faster                                                                                                      |
| xml_etree_process          | 40.0 ms                                                                                                                | 37.0 ms: 1.08x faster                                                                                                      |
| pprint_pformat             | 1.12 sec                                                                                                               | 1.03 sec: 1.08x faster                                                                                                     |
| scimark_sor                | 90.7 ms                                                                                                                | 84.3 ms: 1.08x faster                                                                                                      |
| pickle_pure_python         | 224 us                                                                                                                 | 209 us: 1.07x faster                                                                                                       |
| json_loads                 | 15.7 us                                                                                                                | 14.8 us: 1.06x faster                                                                                                      |
| logging_silent             | 62.5 ns                                                                                                                | 59.0 ns: 1.06x faster                                                                                                      |
| richards_super             | 34.7 ms                                                                                                                | 33.0 ms: 1.05x faster                                                                                                      |
| telco                      | 4.69 ms                                                                                                                | 4.47 ms: 1.05x faster                                                                                                      |
| go                         | 90.3 ms                                                                                                                | 86.2 ms: 1.05x faster                                                                                                      |
| unpickle                   | 8.95 us                                                                                                                | 8.57 us: 1.05x faster                                                                                                      |
| float                      | 46.8 ms                                                                                                                | 44.8 ms: 1.04x faster                                                                                                      |
| unpickle_list              | 2.76 us                                                                                                                | 2.65 us: 1.04x faster                                                                                                      |
| scimark_monte_carlo        | 46.4 ms                                                                                                                | 44.6 ms: 1.04x faster                                                                                                      |
| sqlglot_parse              | 888 us                                                                                                                 | 854 us: 1.04x faster                                                                                                       |
| richards                   | 30.3 ms                                                                                                                | 29.1 ms: 1.04x faster                                                                                                      |
| nqueens                    | 61.2 ms                                                                                                                | 58.9 ms: 1.04x faster                                                                                                      |
| regex_compile              | 86.0 ms                                                                                                                | 82.7 ms: 1.04x faster                                                                                                      |
| pprint_safe_repr           | 549 ms                                                                                                                 | 529 ms: 1.04x faster                                                                                                       |
| k_core                     | 1.69 sec                                                                                                               | 1.63 sec: 1.04x faster                                                                                                     |
| crypto_pyaes               | 48.5 ms                                                                                                                | 46.9 ms: 1.03x faster                                                                                                      |
| xml_etree_iterparse        | 63.1 ms                                                                                                                | 61.1 ms: 1.03x faster                                                                                                      |
| sqlite_synth               | 1.56 us                                                                                                                | 1.52 us: 1.03x faster                                                                                                      |
| meteor_contest             | 75.7 ms                                                                                                                | 73.7 ms: 1.03x faster                                                                                                      |
| json                       | 3.09 ms                                                                                                                | 3.01 ms: 1.03x faster                                                                                                      |
| connected_components       | 322 ms                                                                                                                 | 315 ms: 1.02x faster                                                                                                       |
| unpack_sequence            | 43.9 ns                                                                                                                | 42.9 ns: 1.02x faster                                                                                                      |
| async_tree_io_tg           | 421 ms                                                                                                                 | 413 ms: 1.02x faster                                                                                                       |
| json_dumps                 | 6.68 ms                                                                                                                | 6.55 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 190 ms                                                                                                                 | 186 ms: 1.02x faster                                                                                                       |
| spectral_norm              | 60.7 ms                                                                                                                | 59.6 ms: 1.02x faster                                                                                                      |
| thrift                     | 516 us                                                                                                                 | 506 us: 1.02x faster                                                                                                       |
| sqlglot_transpile          | 1.10 ms                                                                                                                | 1.08 ms: 1.02x faster                                                                                                      |
| asyncio_websockets         | 314 ms                                                                                                                 | 308 ms: 1.02x faster                                                                                                       |
| 2to3                       | 223 ms                                                                                                                 | 219 ms: 1.02x faster                                                                                                       |
| comprehensions             | 11.3 us                                                                                                                | 11.1 us: 1.02x faster                                                                                                      |
| scimark_lu                 | 64.0 ms                                                                                                                | 63.0 ms: 1.02x faster                                                                                                      |
| raytrace                   | 197 ms                                                                                                                 | 194 ms: 1.02x faster                                                                                                       |
| deepcopy                   | 187 us                                                                                                                 | 184 us: 1.02x faster                                                                                                       |
| async_tree_memoization_tg  | 221 ms                                                                                                                 | 218 ms: 1.02x faster                                                                                                       |
| async_tree_none_tg         | 179 ms                                                                                                                 | 177 ms: 1.01x faster                                                                                                       |
| shortest_path              | 352 ms                                                                                                                 | 347 ms: 1.01x faster                                                                                                       |
| coverage                   | 48.1 ms                                                                                                                | 47.5 ms: 1.01x faster                                                                                                      |
| chaos                      | 42.5 ms                                                                                                                | 42.0 ms: 1.01x faster                                                                                                      |
| sympy_sum                  | 89.9 ms                                                                                                                | 89.1 ms: 1.01x faster                                                                                                      |
| mdp                        | 1.55 sec                                                                                                               | 1.54 sec: 1.01x faster                                                                                                     |
| hexiom                     | 4.30 ms                                                                                                                | 4.28 ms: 1.00x faster                                                                                                      |
| deltablue                  | 2.24 ms                                                                                                                | 2.23 ms: 1.00x faster                                                                                                      |
| pidigits                   | 150 ms                                                                                                                 | 150 ms: 1.00x faster                                                                                                       |
| dulwich_log                | 41.6 ms                                                                                                                | 41.8 ms: 1.00x slower                                                                                                      |
| bench_mp_pool              | 83.5 ms                                                                                                                | 83.9 ms: 1.00x slower                                                                                                      |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| pickle_list                | 2.95 us                                                                                                                | 2.97 us: 1.01x slower                                                                                                      |
| sphinx                     | 640 ms                                                                                                                 | 647 ms: 1.01x slower                                                                                                       |
| typing_runtime_protocols   | 110 us                                                                                                                 | 111 us: 1.01x slower                                                                                                       |
| regex_v8                   | 14.3 ms                                                                                                                | 14.5 ms: 1.01x slower                                                                                                      |
| subparsers                 | 16.0 ms                                                                                                                | 16.2 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 343 ms                                                                                                                 | 347 ms: 1.01x slower                                                                                                       |
| deepcopy_reduce            | 1.92 us                                                                                                                | 1.94 us: 1.01x slower                                                                                                      |
| create_gc_cycles           | 1.22 ms                                                                                                                | 1.23 ms: 1.01x slower                                                                                                      |
| sympy_expand               | 302 ms                                                                                                                 | 307 ms: 1.02x slower                                                                                                       |
| regex_effbot               | 1.42 ms                                                                                                                | 1.45 ms: 1.02x slower                                                                                                      |
| generators                 | 19.6 ms                                                                                                                | 20.1 ms: 1.02x slower                                                                                                      |
| coroutines                 | 13.6 ms                                                                                                                | 13.9 ms: 1.02x slower                                                                                                      |
| docutils                   | 1.65 sec                                                                                                               | 1.69 sec: 1.03x slower                                                                                                     |
| genshi_text                | 16.3 ms                                                                                                                | 16.8 ms: 1.03x slower                                                                                                      |
| sqlglot_optimize           | 35.5 ms                                                                                                                | 36.8 ms: 1.04x slower                                                                                                      |
| sqlglot_normalize          | 191 ms                                                                                                                 | 199 ms: 1.04x slower                                                                                                       |
| django_template            | 24.9 ms                                                                                                                | 26.0 ms: 1.04x slower                                                                                                      |
| many_optionals             | 431 us                                                                                                                 | 453 us: 1.05x slower                                                                                                       |
| async_generators           | 222 ms                                                                                                                 | 234 ms: 1.05x slower                                                                                                       |
| genshi_xml                 | 35.3 ms                                                                                                                | 39.1 ms: 1.11x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (18): async_tree_memoization, xml_etree_parse, python_startup_no_site, gc_traversal, async_tree_io, python_startup, logging_format, regex_dna, pickle, pathlib, sympy_integrate, sympy_str, pickle_dict, logging_simple, pycparser, html5lib, bench_thread_pool, pylint

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown