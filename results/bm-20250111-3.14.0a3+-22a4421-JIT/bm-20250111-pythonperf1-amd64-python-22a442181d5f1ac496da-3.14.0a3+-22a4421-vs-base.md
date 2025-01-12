# Results vs. base

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.030x faster
- HPT reliability: 98.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                                                               | 1.74 sec: 1.04x slower                                                                                                     |
| sphinx         | 647 ms                                                                                                                 | 667 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 1.40 sec                                                                                                               | 1.37 sec: 1.03x faster                                                                                                     |
| async_tree_memoization     | 228 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| async_tree_none_tg         | 173 ms                                                                                                                 | 170 ms: 1.02x faster                                                                                                       |
| async_tree_io              | 411 ms                                                                                                                 | 405 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                                                                 | 344 ms: 1.00x faster                                                                                                       |
| coroutines                 | 13.4 ms                                                                                                                | 13.5 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 348 ms                                                                                                                 | 351 ms: 1.01x slower                                                                                                       |
| async_tree_memoization_tg  | 212 ms                                                                                                                 | 216 ms: 1.02x slower                                                                                                       |
| async_generators           | 232 ms                                                                                                                 | 261 ms: 1.12x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (4): async_tree_none, asyncio_websockets, async_tree_io_tg, asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 72.7 ms                                                                                                                | 53.9 ms: 1.35x faster                                                                                                      |
| float          | 49.6 ms                                                                                                                | 39.3 ms: 1.26x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.19x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 85.1 ms                                                                                                                | 79.5 ms: 1.07x faster                                                                                                      |
| regex_dna      | 112 ms                                                                                                                 | 116 ms: 1.03x slower                                                                                                       |
| regex_v8       | 14.5 ms                                                                                                                | 15.0 ms: 1.04x slower                                                                                                      |
| regex_effbot   | 1.42 ms                                                                                                                | 1.48 ms: 1.04x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 143 us                                                                                                                 | 108 us: 1.33x faster                                                                                                       |
| pickle_list          | 3.50 us                                                                                                                | 3.01 us: 1.16x faster                                                                                                      |
| tomli_loads          | 1.38 sec                                                                                                               | 1.19 sec: 1.16x faster                                                                                                     |
| pickle_dict          | 20.6 us                                                                                                                | 18.3 us: 1.13x faster                                                                                                      |
| xml_etree_generate   | 56.5 ms                                                                                                                | 51.2 ms: 1.10x faster                                                                                                      |
| xml_etree_process    | 39.8 ms                                                                                                                | 36.2 ms: 1.10x faster                                                                                                      |
| json_dumps           | 6.63 ms                                                                                                                | 6.28 ms: 1.05x faster                                                                                                      |
| pickle_pure_python   | 219 us                                                                                                                 | 208 us: 1.05x faster                                                                                                       |
| json_loads           | 14.7 us                                                                                                                | 14.3 us: 1.02x faster                                                                                                      |
| pickle               | 8.13 us                                                                                                                | 7.97 us: 1.02x faster                                                                                                      |
| xml_etree_iterparse  | 61.4 ms                                                                                                                | 60.4 ms: 1.02x faster                                                                                                      |
| xml_etree_parse      | 89.5 ms                                                                                                                | 88.5 ms: 1.01x faster                                                                                                      |
| unpickle             | 8.72 us                                                                                                                | 8.85 us: 1.02x slower                                                                                                      |
| unpickle_list        | 2.94 us                                                                                                                | 3.02 us: 1.03x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.08x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.65 ms                                                                                                                | 5.08 ms: 1.31x faster                                                                                                      |
| django_template | 25.1 ms                                                                                                                | 27.5 ms: 1.10x slower                                                                                                      |
| genshi_text     | 16.1 ms                                                                                                                | 18.3 ms: 1.13x slower                                                                                                      |
| genshi_xml      | 35.1 ms                                                                                                                | 46.0 ms: 1.31x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.06x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json | results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| scimark_sor                | 83.1 ms                                                                                                                | 61.3 ms: 1.36x faster                                                                                                      |
| nbody                      | 72.7 ms                                                                                                                | 53.9 ms: 1.35x faster                                                                                                      |
| unpickle_pure_python       | 143 us                                                                                                                 | 108 us: 1.33x faster                                                                                                       |
| mako                       | 6.65 ms                                                                                                                | 5.08 ms: 1.31x faster                                                                                                      |
| scimark_fft                | 185 ms                                                                                                                 | 143 ms: 1.29x faster                                                                                                       |
| float                      | 49.6 ms                                                                                                                | 39.3 ms: 1.26x faster                                                                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                                                                                | 2.04 ms: 1.25x faster                                                                                                      |
| scimark_monte_carlo        | 45.1 ms                                                                                                                | 36.4 ms: 1.24x faster                                                                                                      |
| spectral_norm              | 61.5 ms                                                                                                                | 49.8 ms: 1.24x faster                                                                                                      |
| deepcopy_memo              | 19.8 us                                                                                                                | 16.3 us: 1.22x faster                                                                                                      |
| pickle_list                | 3.50 us                                                                                                                | 3.01 us: 1.16x faster                                                                                                      |
| tomli_loads                | 1.38 sec                                                                                                               | 1.19 sec: 1.16x faster                                                                                                     |
| pyflate                    | 317 ms                                                                                                                 | 276 ms: 1.15x faster                                                                                                       |
| crypto_pyaes               | 47.1 ms                                                                                                                | 41.2 ms: 1.14x faster                                                                                                      |
| pickle_dict                | 20.6 us                                                                                                                | 18.3 us: 1.13x faster                                                                                                      |
| pprint_pformat             | 1.07 sec                                                                                                               | 948 ms: 1.12x faster                                                                                                       |
| pprint_safe_repr           | 531 ms                                                                                                                 | 476 ms: 1.12x faster                                                                                                       |
| scimark_lu                 | 58.6 ms                                                                                                                | 53.0 ms: 1.11x faster                                                                                                      |
| telco                      | 4.81 ms                                                                                                                | 4.35 ms: 1.11x faster                                                                                                      |
| bpe_tokeniser              | 2.94 sec                                                                                                               | 2.66 sec: 1.10x faster                                                                                                     |
| xml_etree_generate         | 56.5 ms                                                                                                                | 51.2 ms: 1.10x faster                                                                                                      |
| xml_etree_process          | 39.8 ms                                                                                                                | 36.2 ms: 1.10x faster                                                                                                      |
| json                       | 3.23 ms                                                                                                                | 2.98 ms: 1.08x faster                                                                                                      |
| regex_compile              | 85.1 ms                                                                                                                | 79.5 ms: 1.07x faster                                                                                                      |
| logging_silent             | 61.1 ns                                                                                                                | 57.0 ns: 1.07x faster                                                                                                      |
| fannkuch                   | 262 ms                                                                                                                 | 247 ms: 1.06x faster                                                                                                       |
| json_dumps                 | 6.63 ms                                                                                                                | 6.28 ms: 1.05x faster                                                                                                      |
| sqlglot_parse              | 862 us                                                                                                                 | 820 us: 1.05x faster                                                                                                       |
| pickle_pure_python         | 219 us                                                                                                                 | 208 us: 1.05x faster                                                                                                       |
| k_core                     | 1.68 sec                                                                                                               | 1.61 sec: 1.04x faster                                                                                                     |
| meteor_contest             | 77.4 ms                                                                                                                | 74.2 ms: 1.04x faster                                                                                                      |
| dulwich_log                | 42.3 ms                                                                                                                | 40.6 ms: 1.04x faster                                                                                                      |
| chaos                      | 42.3 ms                                                                                                                | 41.0 ms: 1.03x faster                                                                                                      |
| connected_components       | 322 ms                                                                                                                 | 313 ms: 1.03x faster                                                                                                       |
| asyncio_tcp_ssl            | 1.40 sec                                                                                                               | 1.37 sec: 1.03x faster                                                                                                     |
| json_loads                 | 14.7 us                                                                                                                | 14.3 us: 1.02x faster                                                                                                      |
| pickle                     | 8.13 us                                                                                                                | 7.97 us: 1.02x faster                                                                                                      |
| shortest_path              | 354 ms                                                                                                                 | 347 ms: 1.02x faster                                                                                                       |
| sqlglot_transpile          | 1.08 ms                                                                                                                | 1.06 ms: 1.02x faster                                                                                                      |
| sqlite_synth               | 1.60 us                                                                                                                | 1.57 us: 1.02x faster                                                                                                      |
| async_tree_memoization     | 228 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| async_tree_none_tg         | 173 ms                                                                                                                 | 170 ms: 1.02x faster                                                                                                       |
| xml_etree_iterparse        | 61.4 ms                                                                                                                | 60.4 ms: 1.02x faster                                                                                                      |
| sympy_expand               | 302 ms                                                                                                                 | 297 ms: 1.02x faster                                                                                                       |
| comprehensions             | 11.8 us                                                                                                                | 11.6 us: 1.01x faster                                                                                                      |
| async_tree_io              | 411 ms                                                                                                                 | 405 ms: 1.01x faster                                                                                                       |
| sympy_str                  | 176 ms                                                                                                                 | 174 ms: 1.01x faster                                                                                                       |
| xml_etree_parse            | 89.5 ms                                                                                                                | 88.5 ms: 1.01x faster                                                                                                      |
| logging_simple             | 6.27 us                                                                                                                | 6.21 us: 1.01x faster                                                                                                      |
| deepcopy_reduce            | 1.85 us                                                                                                                | 1.83 us: 1.01x faster                                                                                                      |
| logging_format             | 6.67 us                                                                                                                | 6.62 us: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 345 ms                                                                                                                 | 344 ms: 1.00x faster                                                                                                       |
| coroutines                 | 13.4 ms                                                                                                                | 13.5 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed    | 348 ms                                                                                                                 | 351 ms: 1.01x slower                                                                                                       |
| sympy_integrate            | 13.2 ms                                                                                                                | 13.4 ms: 1.01x slower                                                                                                      |
| sympy_sum                  | 89.4 ms                                                                                                                | 90.5 ms: 1.01x slower                                                                                                      |
| unpickle                   | 8.72 us                                                                                                                | 8.85 us: 1.02x slower                                                                                                      |
| async_tree_memoization_tg  | 212 ms                                                                                                                 | 216 ms: 1.02x slower                                                                                                       |
| thrift                     | 520 us                                                                                                                 | 529 us: 1.02x slower                                                                                                       |
| coverage                   | 46.9 ms                                                                                                                | 47.7 ms: 1.02x slower                                                                                                      |
| deltablue                  | 2.22 ms                                                                                                                | 2.28 ms: 1.03x slower                                                                                                      |
| unpickle_list              | 2.94 us                                                                                                                | 3.02 us: 1.03x slower                                                                                                      |
| nqueens                    | 61.8 ms                                                                                                                | 63.5 ms: 1.03x slower                                                                                                      |
| sphinx                     | 647 ms                                                                                                                 | 667 ms: 1.03x slower                                                                                                       |
| regex_dna                  | 112 ms                                                                                                                 | 116 ms: 1.03x slower                                                                                                       |
| many_optionals             | 438 us                                                                                                                 | 453 us: 1.03x slower                                                                                                       |
| regex_v8                   | 14.5 ms                                                                                                                | 15.0 ms: 1.04x slower                                                                                                      |
| docutils                   | 1.67 sec                                                                                                               | 1.74 sec: 1.04x slower                                                                                                     |
| sqlglot_optimize           | 35.6 ms                                                                                                                | 37.1 ms: 1.04x slower                                                                                                      |
| regex_effbot               | 1.42 ms                                                                                                                | 1.48 ms: 1.04x slower                                                                                                      |
| sqlglot_normalize          | 193 ms                                                                                                                 | 202 ms: 1.04x slower                                                                                                       |
| raytrace                   | 192 ms                                                                                                                 | 200 ms: 1.05x slower                                                                                                       |
| deepcopy                   | 180 us                                                                                                                 | 188 us: 1.05x slower                                                                                                       |
| pylint                     | 201 ms                                                                                                                 | 211 ms: 1.05x slower                                                                                                       |
| go                         | 84.1 ms                                                                                                                | 89.8 ms: 1.07x slower                                                                                                      |
| richards_super             | 34.9 ms                                                                                                                | 37.9 ms: 1.08x slower                                                                                                      |
| richards                   | 30.9 ms                                                                                                                | 33.6 ms: 1.09x slower                                                                                                      |
| django_template            | 25.1 ms                                                                                                                | 27.5 ms: 1.10x slower                                                                                                      |
| unpack_sequence            | 37.6 ns                                                                                                                | 41.5 ns: 1.10x slower                                                                                                      |
| generators                 | 21.4 ms                                                                                                                | 23.7 ms: 1.11x slower                                                                                                      |
| async_generators           | 232 ms                                                                                                                 | 261 ms: 1.12x slower                                                                                                       |
| genshi_text                | 16.1 ms                                                                                                                | 18.3 ms: 1.13x slower                                                                                                      |
| hexiom                     | 4.25 ms                                                                                                                | 5.00 ms: 1.18x slower                                                                                                      |
| genshi_xml                 | 35.1 ms                                                                                                                | 46.0 ms: 1.31x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (18): async_tree_none, asyncio_websockets, subparsers, async_tree_io_tg, create_gc_cycles, mdp, asyncio_tcp, pidigits, typing_runtime_protocols, html5lib, python_startup, bench_mp_pool, python_startup_no_site, pathlib, gc_traversal, 2to3, pycparser, bench_thread_pool

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 98.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown