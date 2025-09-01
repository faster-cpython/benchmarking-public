# Results vs. base

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.035x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.58 sec                                                                                                             | 1.62 sec: 1.02x slower                                                                                                   |
| sphinx         | 612 ms                                                                                                               | 624 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.01x slower                                                                                                             |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| coroutines              | 14.7 ms                                                                                                              | 14.0 ms: 1.05x faster                                                                                                    |
| async_tree_io_tg        | 397 ms                                                                                                               | 380 ms: 1.04x faster                                                                                                     |
| async_tree_memoization  | 205 ms                                                                                                               | 200 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg      | 171 ms                                                                                                               | 166 ms: 1.03x faster                                                                                                     |
| async_tree_none         | 174 ms                                                                                                               | 171 ms: 1.02x faster                                                                                                     |
| async_tree_io           | 392 ms                                                                                                               | 386 ms: 1.02x faster                                                                                                     |
| async_tree_cpu_io_mixed | 326 ms                                                                                                               | 330 ms: 1.01x slower                                                                                                     |
| asyncio_websockets      | 157 ms                                                                                                               | 162 ms: 1.03x slower                                                                                                     |
| asyncio_tcp_ssl         | 1.28 sec                                                                                                             | 1.32 sec: 1.03x slower                                                                                                   |
| async_generators        | 230 ms                                                                                                               | 242 ms: 1.05x slower                                                                                                     |
| asyncio_tcp             | 420 ms                                                                                                               | 455 ms: 1.08x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.00x slower                                                                                                             |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                                                              | 52.3 ms: 1.25x faster                                                                                                    |
| float          | 45.0 ms                                                                                                              | 42.8 ms: 1.05x faster                                                                                                    |
| pidigits       | 146 ms                                                                                                               | 144 ms: 1.02x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.10x faster                                                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 13.1 ms                                                                                                              | 13.7 ms: 1.04x slower                                                                                                    |
| regex_effbot   | 1.45 ms                                                                                                              | 1.52 ms: 1.05x slower                                                                                                    |
| regex_dna      | 113 ms                                                                                                               | 118 ms: 1.05x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                | 1.03x slower                                                                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                                                               | 105 us: 1.28x faster                                                                                                     |
| tomli_loads          | 1.39 sec                                                                                                             | 1.09 sec: 1.28x faster                                                                                                   |
| xml_etree_generate   | 56.5 ms                                                                                                              | 49.6 ms: 1.14x faster                                                                                                    |
| xml_etree_process    | 38.9 ms                                                                                                              | 35.1 ms: 1.11x faster                                                                                                    |
| unpickle_list        | 2.96 us                                                                                                              | 2.70 us: 1.09x faster                                                                                                    |
| pickle_pure_python   | 212 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| pickle               | 7.73 us                                                                                                              | 7.53 us: 1.03x faster                                                                                                    |
| xml_etree_iterparse  | 63.5 ms                                                                                                              | 62.0 ms: 1.02x faster                                                                                                    |
| pickle_list          | 3.26 us                                                                                                              | 3.19 us: 1.02x faster                                                                                                    |
| unpickle             | 8.31 us                                                                                                              | 8.38 us: 1.01x slower                                                                                                    |
| json_dumps           | 5.41 ms                                                                                                              | 5.48 ms: 1.01x slower                                                                                                    |
| xml_etree_parse      | 85.4 ms                                                                                                              | 87.8 ms: 1.03x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                                | 1.06x faster                                                                                                             |

Benchmark hidden because not significant (2): json_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-----------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.79 ms                                                                                                              | 5.25 ms: 1.29x faster                                                                                                    |
| genshi_xml      | 34.5 ms                                                                                                              | 34.0 ms: 1.02x faster                                                                                                    |
| django_template | 24.2 ms                                                                                                              | 23.8 ms: 1.01x faster                                                                                                    |
| Geometric mean  | (ref)                                                                                                                | 1.08x faster                                                                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf1-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------|:--------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------:|
| mako                    | 6.79 ms                                                                                                              | 5.25 ms: 1.29x faster                                                                                                    |
| unpickle_pure_python    | 135 us                                                                                                               | 105 us: 1.28x faster                                                                                                     |
| tomli_loads             | 1.39 sec                                                                                                             | 1.09 sec: 1.28x faster                                                                                                   |
| fannkuch                | 269 ms                                                                                                               | 211 ms: 1.27x faster                                                                                                     |
| scimark_fft             | 184 ms                                                                                                               | 146 ms: 1.26x faster                                                                                                     |
| nbody                   | 65.3 ms                                                                                                              | 52.3 ms: 1.25x faster                                                                                                    |
| bpe_tokeniser           | 2.96 sec                                                                                                             | 2.47 sec: 1.20x faster                                                                                                   |
| pprint_pformat          | 1.00 sec                                                                                                             | 849 ms: 1.18x faster                                                                                                     |
| pprint_safe_repr        | 495 ms                                                                                                               | 424 ms: 1.17x faster                                                                                                     |
| scimark_sparse_mat_mult | 2.56 ms                                                                                                              | 2.23 ms: 1.15x faster                                                                                                    |
| xml_etree_generate      | 56.5 ms                                                                                                              | 49.6 ms: 1.14x faster                                                                                                    |
| xml_etree_process       | 38.9 ms                                                                                                              | 35.1 ms: 1.11x faster                                                                                                    |
| unpack_sequence         | 37.8 ns                                                                                                              | 34.2 ns: 1.10x faster                                                                                                    |
| pyflate                 | 287 ms                                                                                                               | 260 ms: 1.10x faster                                                                                                     |
| telco                   | 4.10 ms                                                                                                              | 3.75 ms: 1.09x faster                                                                                                    |
| unpickle_list           | 2.96 us                                                                                                              | 2.70 us: 1.09x faster                                                                                                    |
| sqlglot_v2_parse        | 829 us                                                                                                               | 761 us: 1.09x faster                                                                                                     |
| comprehensions          | 11.0 us                                                                                                              | 10.3 us: 1.07x faster                                                                                                    |
| sqlglot_v2_transpile    | 1.03 ms                                                                                                              | 968 us: 1.06x faster                                                                                                     |
| crypto_pyaes            | 47.5 ms                                                                                                              | 44.9 ms: 1.06x faster                                                                                                    |
| float                   | 45.0 ms                                                                                                              | 42.8 ms: 1.05x faster                                                                                                    |
| nqueens                 | 62.1 ms                                                                                                              | 59.1 ms: 1.05x faster                                                                                                    |
| pickle_pure_python      | 212 us                                                                                                               | 203 us: 1.05x faster                                                                                                     |
| coroutines              | 14.7 ms                                                                                                              | 14.0 ms: 1.05x faster                                                                                                    |
| async_tree_io_tg        | 397 ms                                                                                                               | 380 ms: 1.04x faster                                                                                                     |
| spectral_norm           | 64.8 ms                                                                                                              | 62.1 ms: 1.04x faster                                                                                                    |
| connected_components    | 329 ms                                                                                                               | 315 ms: 1.04x faster                                                                                                     |
| logging_silent          | 56.4 ns                                                                                                              | 54.1 ns: 1.04x faster                                                                                                    |
| k_core                  | 1.64 sec                                                                                                             | 1.59 sec: 1.03x faster                                                                                                   |
| json                    | 2.97 ms                                                                                                              | 2.88 ms: 1.03x faster                                                                                                    |
| sqlite_synth            | 1.57 us                                                                                                              | 1.53 us: 1.03x faster                                                                                                    |
| raytrace                | 177 ms                                                                                                               | 172 ms: 1.03x faster                                                                                                     |
| async_tree_memoization  | 205 ms                                                                                                               | 200 ms: 1.03x faster                                                                                                     |
| async_tree_none_tg      | 171 ms                                                                                                               | 166 ms: 1.03x faster                                                                                                     |
| pickle                  | 7.73 us                                                                                                              | 7.53 us: 1.03x faster                                                                                                    |
| richards                | 27.8 ms                                                                                                              | 27.1 ms: 1.03x faster                                                                                                    |
| coverage                | 50.6 ms                                                                                                              | 49.3 ms: 1.03x faster                                                                                                    |
| shortest_path           | 357 ms                                                                                                               | 348 ms: 1.03x faster                                                                                                     |
| xml_etree_iterparse     | 63.5 ms                                                                                                              | 62.0 ms: 1.02x faster                                                                                                    |
| chaos                   | 41.2 ms                                                                                                              | 40.2 ms: 1.02x faster                                                                                                    |
| pickle_list             | 3.26 us                                                                                                              | 3.19 us: 1.02x faster                                                                                                    |
| gc_traversal            | 2.15 ms                                                                                                              | 2.11 ms: 1.02x faster                                                                                                    |
| async_tree_none         | 174 ms                                                                                                               | 171 ms: 1.02x faster                                                                                                     |
| genshi_xml              | 34.5 ms                                                                                                              | 34.0 ms: 1.02x faster                                                                                                    |
| meteor_contest          | 72.3 ms                                                                                                              | 71.1 ms: 1.02x faster                                                                                                    |
| async_tree_io           | 392 ms                                                                                                               | 386 ms: 1.02x faster                                                                                                     |
| pidigits                | 146 ms                                                                                                               | 144 ms: 1.02x faster                                                                                                     |
| django_template         | 24.2 ms                                                                                                              | 23.8 ms: 1.01x faster                                                                                                    |
| mdp                     | 793 ms                                                                                                               | 783 ms: 1.01x faster                                                                                                     |
| scimark_monte_carlo     | 40.7 ms                                                                                                              | 40.2 ms: 1.01x faster                                                                                                    |
| sympy_sum               | 85.2 ms                                                                                                              | 84.4 ms: 1.01x faster                                                                                                    |
| scimark_sor             | 78.7 ms                                                                                                              | 78.2 ms: 1.01x faster                                                                                                    |
| sqlglot_v2_optimize     | 33.8 ms                                                                                                              | 34.0 ms: 1.01x slower                                                                                                    |
| hexiom                  | 4.11 ms                                                                                                              | 4.13 ms: 1.01x slower                                                                                                    |
| dulwich_log             | 38.5 ms                                                                                                              | 38.7 ms: 1.01x slower                                                                                                    |
| unpickle                | 8.31 us                                                                                                              | 8.38 us: 1.01x slower                                                                                                    |
| deepcopy                | 168 us                                                                                                               | 170 us: 1.01x slower                                                                                                     |
| async_tree_cpu_io_mixed | 326 ms                                                                                                               | 330 ms: 1.01x slower                                                                                                     |
| deltablue               | 2.18 ms                                                                                                              | 2.21 ms: 1.01x slower                                                                                                    |
| json_dumps              | 5.41 ms                                                                                                              | 5.48 ms: 1.01x slower                                                                                                    |
| sphinx                  | 612 ms                                                                                                               | 624 ms: 1.02x slower                                                                                                     |
| thrift                  | 484 us                                                                                                               | 495 us: 1.02x slower                                                                                                     |
| sympy_integrate         | 12.2 ms                                                                                                              | 12.5 ms: 1.02x slower                                                                                                    |
| docutils                | 1.58 sec                                                                                                             | 1.62 sec: 1.02x slower                                                                                                   |
| sympy_expand            | 283 ms                                                                                                               | 291 ms: 1.03x slower                                                                                                     |
| xml_etree_parse         | 85.4 ms                                                                                                              | 87.8 ms: 1.03x slower                                                                                                    |
| asyncio_websockets      | 157 ms                                                                                                               | 162 ms: 1.03x slower                                                                                                     |
| asyncio_tcp_ssl         | 1.28 sec                                                                                                             | 1.32 sec: 1.03x slower                                                                                                   |
| regex_v8                | 13.1 ms                                                                                                              | 13.7 ms: 1.04x slower                                                                                                    |
| deepcopy_memo           | 18.3 us                                                                                                              | 19.1 us: 1.04x slower                                                                                                    |
| regex_effbot            | 1.45 ms                                                                                                              | 1.52 ms: 1.05x slower                                                                                                    |
| regex_dna               | 113 ms                                                                                                               | 118 ms: 1.05x slower                                                                                                     |
| async_generators        | 230 ms                                                                                                               | 242 ms: 1.05x slower                                                                                                     |
| asyncio_tcp             | 420 ms                                                                                                               | 455 ms: 1.08x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                | 1.03x faster                                                                                                             |

Benchmark hidden because not significant (28): async_tree_memoization_tg, python_startup_no_site, logging_simple, bench_thread_pool, regex_compile, 2to3, html5lib, genshi_text, sympy_str, create_gc_cycles, scimark_lu, json_loads, pathlib, sqlglot_v2_normalize, generators, pycparser, typing_runtime_protocols, bench_mp_pool, richards_super, async_tree_cpu_io_mixed_tg, pylint, logging_format, go, subparsers, python_startup, pickle_dict, many_optionals, deepcopy_reduce

- Geometric mean (including insignificant results): 1.035x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown