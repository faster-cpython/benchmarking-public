# Results vs. base

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.010x faster
- HPT reliability: 62.27%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                                                                               | 223 ms: 1.02x slower                                                                                                     |
| docutils       | 1.60 sec                                                                                                             | 1.66 sec: 1.04x slower                                                                                                   |
| html5lib       | 37.8 ms                                                                                                              | 38.6 ms: 1.02x slower                                                                                                    |
| sphinx         | 634 ms                                                                                                               | 644 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.02x slower                                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 396 ms                                                                                                               | 384 ms: 1.03x faster                                                                                                     |
| asyncio_websockets         | 159 ms                                                                                                               | 156 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                               | 334 ms: 1.02x faster                                                                                                     |
| async_tree_none_tg         | 170 ms                                                                                                               | 168 ms: 1.01x faster                                                                                                     |
| async_tree_none            | 168 ms                                                                                                               | 167 ms: 1.01x faster                                                                                                     |
| async_tree_memoization     | 202 ms                                                                                                               | 204 ms: 1.01x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.40 sec                                                                                                             | 1.42 sec: 1.01x slower                                                                                                   |
| asyncio_tcp                | 500 ms                                                                                                               | 521 ms: 1.04x slower                                                                                                     |
| coroutines                 | 14.0 ms                                                                                                              | 14.7 ms: 1.05x slower                                                                                                    |
| async_generators           | 231 ms                                                                                                               | 252 ms: 1.09x slower                                                                                                     |
| Geometric mean             | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 64.2 ms                                                                                                              | 54.7 ms: 1.18x faster                                                                                                    |
| float          | 42.9 ms                                                                                                              | 44.5 ms: 1.04x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 14.1 ms                                                                                                              | 13.9 ms: 1.02x faster                                                                                                    |
| regex_compile  | 78.5 ms                                                                                                              | 79.1 ms: 1.01x slower                                                                                                    |
| regex_effbot   | 1.50 ms                                                                                                              | 1.61 ms: 1.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 132 us                                                                                                               | 107 us: 1.23x faster                                                                                                     |
| tomli_loads          | 1.35 sec                                                                                                             | 1.14 sec: 1.18x faster                                                                                                   |
| xml_etree_generate   | 55.5 ms                                                                                                              | 51.1 ms: 1.09x faster                                                                                                    |
| xml_etree_process    | 38.4 ms                                                                                                              | 36.1 ms: 1.06x faster                                                                                                    |
| xml_etree_iterparse  | 64.7 ms                                                                                                              | 61.7 ms: 1.05x faster                                                                                                    |
| unpickle_list        | 2.84 us                                                                                                              | 2.77 us: 1.03x faster                                                                                                    |
| pickle               | 8.08 us                                                                                                              | 7.88 us: 1.03x faster                                                                                                    |
| pickle_dict          | 20.5 us                                                                                                              | 20.1 us: 1.02x faster                                                                                                    |
| pickle_pure_python   | 206 us                                                                                                               | 204 us: 1.01x faster                                                                                                     |
| json_dumps           | 6.18 ms                                                                                                              | 6.28 ms: 1.02x slower                                                                                                    |
| pickle_list          | 3.33 us                                                                                                              | 3.39 us: 1.02x slower                                                                                                    |
| unpickle             | 8.41 us                                                                                                              | 8.61 us: 1.02x slower                                                                                                    |
| json_loads           | 14.1 us                                                                                                              | 14.6 us: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.04x faster                                                                                                             |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 26.0 ms                                                                                                              | 25.5 ms: 1.02x faster                                                                                                    |
| python_startup_no_site | 19.5 ms                                                                                                              | 19.2 ms: 1.01x faster                                                                                                    |
| Geometric mean         | (ref)                                                                                                                | 1.02x faster                                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.57 ms                                                                                                              | 5.35 ms: 1.23x faster                                                                                                    |
| genshi_text     | 15.5 ms                                                                                                              | 15.8 ms: 1.02x slower                                                                                                    |
| django_template | 24.4 ms                                                                                                              | 25.0 ms: 1.03x slower                                                                                                    |
| genshi_xml      | 34.6 ms                                                                                                              | 36.3 ms: 1.05x slower                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.03x faster                                                                                                             |

All benchmarks:
===============

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python       | 132 us                                                                                                               | 107 us: 1.23x faster                                                                                                     |
| mako                       | 6.57 ms                                                                                                              | 5.35 ms: 1.23x faster                                                                                                    |
| scimark_fft                | 181 ms                                                                                                               | 153 ms: 1.18x faster                                                                                                     |
| tomli_loads                | 1.35 sec                                                                                                             | 1.14 sec: 1.18x faster                                                                                                   |
| nbody                      | 64.2 ms                                                                                                              | 54.7 ms: 1.18x faster                                                                                                    |
| fannkuch                   | 258 ms                                                                                                               | 220 ms: 1.17x faster                                                                                                     |
| pyflate                    | 290 ms                                                                                                               | 252 ms: 1.15x faster                                                                                                     |
| bpe_tokeniser              | 2.92 sec                                                                                                             | 2.58 sec: 1.13x faster                                                                                                   |
| scimark_sparse_mat_mult    | 2.48 ms                                                                                                              | 2.25 ms: 1.10x faster                                                                                                    |
| xml_etree_generate         | 55.5 ms                                                                                                              | 51.1 ms: 1.09x faster                                                                                                    |
| pprint_safe_repr           | 492 ms                                                                                                               | 458 ms: 1.07x faster                                                                                                     |
| pprint_pformat             | 1.01 sec                                                                                                             | 944 ms: 1.06x faster                                                                                                     |
| xml_etree_process          | 38.4 ms                                                                                                              | 36.1 ms: 1.06x faster                                                                                                    |
| k_core                     | 1.71 sec                                                                                                             | 1.62 sec: 1.06x faster                                                                                                   |
| xml_etree_iterparse        | 64.7 ms                                                                                                              | 61.7 ms: 1.05x faster                                                                                                    |
| sqlglot_v2_parse           | 820 us                                                                                                               | 784 us: 1.05x faster                                                                                                     |
| crypto_pyaes               | 47.2 ms                                                                                                              | 45.4 ms: 1.04x faster                                                                                                    |
| async_tree_io_tg           | 396 ms                                                                                                               | 384 ms: 1.03x faster                                                                                                     |
| deepcopy_memo              | 19.3 us                                                                                                              | 18.7 us: 1.03x faster                                                                                                    |
| unpickle_list              | 2.84 us                                                                                                              | 2.77 us: 1.03x faster                                                                                                    |
| sqlglot_v2_transpile       | 1.02 ms                                                                                                              | 989 us: 1.03x faster                                                                                                     |
| pickle                     | 8.08 us                                                                                                              | 7.88 us: 1.03x faster                                                                                                    |
| meteor_contest             | 72.4 ms                                                                                                              | 70.9 ms: 1.02x faster                                                                                                    |
| logging_format             | 6.71 us                                                                                                              | 6.57 us: 1.02x faster                                                                                                    |
| pickle_dict                | 20.5 us                                                                                                              | 20.1 us: 1.02x faster                                                                                                    |
| python_startup             | 26.0 ms                                                                                                              | 25.5 ms: 1.02x faster                                                                                                    |
| asyncio_websockets         | 159 ms                                                                                                               | 156 ms: 1.02x faster                                                                                                     |
| pycparser                  | 709 ms                                                                                                               | 696 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed_tg | 340 ms                                                                                                               | 334 ms: 1.02x faster                                                                                                     |
| sqlite_synth               | 1.58 us                                                                                                              | 1.56 us: 1.02x faster                                                                                                    |
| regex_v8                   | 14.1 ms                                                                                                              | 13.9 ms: 1.02x faster                                                                                                    |
| telco                      | 4.48 ms                                                                                                              | 4.41 ms: 1.01x faster                                                                                                    |
| python_startup_no_site     | 19.5 ms                                                                                                              | 19.2 ms: 1.01x faster                                                                                                    |
| async_tree_none_tg         | 170 ms                                                                                                               | 168 ms: 1.01x faster                                                                                                     |
| connected_components       | 331 ms                                                                                                               | 327 ms: 1.01x faster                                                                                                     |
| shortest_path              | 363 ms                                                                                                               | 358 ms: 1.01x faster                                                                                                     |
| comprehensions             | 10.7 us                                                                                                              | 10.6 us: 1.01x faster                                                                                                    |
| pickle_pure_python         | 206 us                                                                                                               | 204 us: 1.01x faster                                                                                                     |
| logging_simple             | 6.21 us                                                                                                              | 6.16 us: 1.01x faster                                                                                                    |
| async_tree_none            | 168 ms                                                                                                               | 167 ms: 1.01x faster                                                                                                     |
| bench_mp_pool              | 93.9 ms                                                                                                              | 94.4 ms: 1.01x slower                                                                                                    |
| regex_compile              | 78.5 ms                                                                                                              | 79.1 ms: 1.01x slower                                                                                                    |
| thrift                     | 496 us                                                                                                               | 501 us: 1.01x slower                                                                                                     |
| raytrace                   | 180 ms                                                                                                               | 182 ms: 1.01x slower                                                                                                     |
| coverage                   | 50.4 ms                                                                                                              | 50.9 ms: 1.01x slower                                                                                                    |
| async_tree_memoization     | 202 ms                                                                                                               | 204 ms: 1.01x slower                                                                                                     |
| asyncio_tcp_ssl            | 1.40 sec                                                                                                             | 1.42 sec: 1.01x slower                                                                                                   |
| deepcopy_reduce            | 1.81 us                                                                                                              | 1.83 us: 1.01x slower                                                                                                    |
| sympy_sum                  | 86.3 ms                                                                                                              | 87.6 ms: 1.02x slower                                                                                                    |
| gc_traversal               | 2.10 ms                                                                                                              | 2.13 ms: 1.02x slower                                                                                                    |
| sphinx                     | 634 ms                                                                                                               | 644 ms: 1.02x slower                                                                                                     |
| json_dumps                 | 6.18 ms                                                                                                              | 6.28 ms: 1.02x slower                                                                                                    |
| pickle_list                | 3.33 us                                                                                                              | 3.39 us: 1.02x slower                                                                                                    |
| richards                   | 26.9 ms                                                                                                              | 27.4 ms: 1.02x slower                                                                                                    |
| 2to3                       | 218 ms                                                                                                               | 223 ms: 1.02x slower                                                                                                     |
| hexiom                     | 4.03 ms                                                                                                              | 4.12 ms: 1.02x slower                                                                                                    |
| subparsers                 | 16.8 ms                                                                                                              | 17.2 ms: 1.02x slower                                                                                                    |
| unpack_sequence            | 36.9 ns                                                                                                              | 37.7 ns: 1.02x slower                                                                                                    |
| html5lib                   | 37.8 ms                                                                                                              | 38.6 ms: 1.02x slower                                                                                                    |
| sqlglot_v2_optimize        | 34.0 ms                                                                                                              | 34.8 ms: 1.02x slower                                                                                                    |
| unpickle                   | 8.41 us                                                                                                              | 8.61 us: 1.02x slower                                                                                                    |
| deepcopy                   | 169 us                                                                                                               | 173 us: 1.02x slower                                                                                                     |
| genshi_text                | 15.5 ms                                                                                                              | 15.8 ms: 1.02x slower                                                                                                    |
| sympy_str                  | 167 ms                                                                                                               | 171 ms: 1.03x slower                                                                                                     |
| django_template            | 24.4 ms                                                                                                              | 25.0 ms: 1.03x slower                                                                                                    |
| sympy_integrate            | 12.3 ms                                                                                                              | 12.7 ms: 1.03x slower                                                                                                    |
| richards_super             | 30.5 ms                                                                                                              | 31.4 ms: 1.03x slower                                                                                                    |
| many_optionals             | 432 us                                                                                                               | 447 us: 1.03x slower                                                                                                     |
| json_loads                 | 14.1 us                                                                                                              | 14.6 us: 1.03x slower                                                                                                    |
| json                       | 2.95 ms                                                                                                              | 3.05 ms: 1.04x slower                                                                                                    |
| typing_runtime_protocols   | 101 us                                                                                                               | 105 us: 1.04x slower                                                                                                     |
| float                      | 42.9 ms                                                                                                              | 44.5 ms: 1.04x slower                                                                                                    |
| docutils                   | 1.60 sec                                                                                                             | 1.66 sec: 1.04x slower                                                                                                   |
| asyncio_tcp                | 500 ms                                                                                                               | 521 ms: 1.04x slower                                                                                                     |
| spectral_norm              | 64.5 ms                                                                                                              | 67.3 ms: 1.04x slower                                                                                                    |
| deltablue                  | 2.14 ms                                                                                                              | 2.24 ms: 1.05x slower                                                                                                    |
| sympy_expand               | 285 ms                                                                                                               | 298 ms: 1.05x slower                                                                                                     |
| go                         | 74.6 ms                                                                                                              | 78.2 ms: 1.05x slower                                                                                                    |
| coroutines                 | 14.0 ms                                                                                                              | 14.7 ms: 1.05x slower                                                                                                    |
| genshi_xml                 | 34.6 ms                                                                                                              | 36.3 ms: 1.05x slower                                                                                                    |
| generators                 | 19.2 ms                                                                                                              | 20.3 ms: 1.06x slower                                                                                                    |
| scimark_monte_carlo        | 40.7 ms                                                                                                              | 43.3 ms: 1.06x slower                                                                                                    |
| scimark_sor                | 74.9 ms                                                                                                              | 80.6 ms: 1.08x slower                                                                                                    |
| regex_effbot               | 1.50 ms                                                                                                              | 1.61 ms: 1.08x slower                                                                                                    |
| async_generators           | 231 ms                                                                                                               | 252 ms: 1.09x slower                                                                                                     |
| scimark_lu                 | 57.0 ms                                                                                                              | 62.4 ms: 1.10x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                                | 1.01x faster                                                                                                             |

Benchmark hidden because not significant (16): nqueens, async_tree_io, regex_dna, pathlib, mdp, chaos, bench_thread_pool, create_gc_cycles, xml_etree_parse, logging_silent, async_tree_cpu_io_mixed, pidigits, dulwich_log, sqlglot_v2_normalize, async_tree_memoization_tg, pylint

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 62.27% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown