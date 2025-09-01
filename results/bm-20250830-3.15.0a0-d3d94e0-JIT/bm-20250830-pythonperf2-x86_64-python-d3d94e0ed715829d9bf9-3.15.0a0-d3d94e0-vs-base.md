# Results vs. base

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.005x faster
- HPT reliability: 63.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                                                                | 285 ms: 1.02x slower                                                                                                      |
| docutils       | 2.87 sec                                                                                                              | 2.90 sec: 1.01x slower                                                                                                    |
| html5lib       | 67.3 ms                                                                                                               | 66.4 ms: 1.01x faster                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|--------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets | 385 ms                                                                                                                | 381 ms: 1.01x faster                                                                                                      |
| asyncio_tcp        | 368 ms                                                                                                                | 370 ms: 1.01x slower                                                                                                      |
| asyncio_tcp_ssl    | 1.58 sec                                                                                                              | 1.59 sec: 1.01x slower                                                                                                    |
| async_tree_none    | 268 ms                                                                                                                | 270 ms: 1.01x slower                                                                                                      |
| coroutines         | 22.0 ms                                                                                                               | 22.6 ms: 1.03x slower                                                                                                     |
| async_generators   | 421 ms                                                                                                                | 437 ms: 1.04x slower                                                                                                      |
| Geometric mean     | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 68.5 ms                                                                                                               | 63.1 ms: 1.09x faster                                                                                                     |
| nbody          | 93.2 ms                                                                                                               | 104 ms: 1.11x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                 | 1.01x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 226 ms                                                                                                                | 224 ms: 1.01x faster                                                                                                      |
| regex_effbot   | 3.56 ms                                                                                                               | 3.53 ms: 1.01x faster                                                                                                     |
| regex_v8       | 23.4 ms                                                                                                               | 23.9 ms: 1.02x slower                                                                                                     |
| Geometric mean | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 206 us                                                                                                                | 195 us: 1.05x faster                                                                                                      |
| tomli_loads          | 1.99 sec                                                                                                              | 1.90 sec: 1.05x faster                                                                                                    |
| xml_etree_process    | 57.5 ms                                                                                                               | 54.9 ms: 1.05x faster                                                                                                     |
| xml_etree_generate   | 82.5 ms                                                                                                               | 79.6 ms: 1.04x faster                                                                                                     |
| pickle_list          | 5.07 us                                                                                                               | 4.92 us: 1.03x faster                                                                                                     |
| pickle_dict          | 33.7 us                                                                                                               | 32.9 us: 1.02x faster                                                                                                     |
| json_dumps           | 10.2 ms                                                                                                               | 10.1 ms: 1.01x faster                                                                                                     |
| pickle_pure_python   | 325 us                                                                                                                | 326 us: 1.00x slower                                                                                                      |
| pickle               | 12.1 us                                                                                                               | 12.3 us: 1.02x slower                                                                                                     |
| xml_etree_iterparse  | 96.8 ms                                                                                                               | 98.3 ms: 1.02x slower                                                                                                     |
| xml_etree_parse      | 137 ms                                                                                                                | 140 ms: 1.02x slower                                                                                                      |
| unpickle_list        | 4.97 us                                                                                                               | 5.11 us: 1.03x slower                                                                                                     |
| Geometric mean       | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

Benchmark hidden because not significant (2): json_loads, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site | 8.80 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                                 | 1.00x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                                                                               | 9.89 ms: 1.09x faster                                                                                                     |
| genshi_text     | 22.7 ms                                                                                                               | 22.9 ms: 1.01x slower                                                                                                     |
| django_template | 34.7 ms                                                                                                               | 35.1 ms: 1.01x slower                                                                                                     |
| genshi_xml      | 52.9 ms                                                                                                               | 53.8 ms: 1.02x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                                 | 1.01x faster                                                                                                              |

All benchmarks:
===============

| Benchmark               | results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json | results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json |
|-------------------------|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| richards_super          | 50.6 ms                                                                                                               | 38.5 ms: 1.31x faster                                                                                                     |
| richards                | 44.1 ms                                                                                                               | 34.0 ms: 1.30x faster                                                                                                     |
| spectral_norm           | 87.4 ms                                                                                                               | 77.6 ms: 1.13x faster                                                                                                     |
| deltablue               | 3.16 ms                                                                                                               | 2.84 ms: 1.11x faster                                                                                                     |
| mako                    | 10.7 ms                                                                                                               | 9.89 ms: 1.09x faster                                                                                                     |
| float                   | 68.5 ms                                                                                                               | 63.1 ms: 1.09x faster                                                                                                     |
| unpickle_pure_python    | 206 us                                                                                                                | 195 us: 1.05x faster                                                                                                      |
| tomli_loads             | 1.99 sec                                                                                                              | 1.90 sec: 1.05x faster                                                                                                    |
| pycparser               | 1.26 sec                                                                                                              | 1.20 sec: 1.05x faster                                                                                                    |
| xml_etree_process       | 57.5 ms                                                                                                               | 54.9 ms: 1.05x faster                                                                                                     |
| pprint_pformat          | 1.57 sec                                                                                                              | 1.50 sec: 1.04x faster                                                                                                    |
| pprint_safe_repr        | 773 ms                                                                                                                | 741 ms: 1.04x faster                                                                                                      |
| generators              | 29.9 ms                                                                                                               | 28.8 ms: 1.04x faster                                                                                                     |
| xml_etree_generate      | 82.5 ms                                                                                                               | 79.6 ms: 1.04x faster                                                                                                     |
| k_core                  | 2.09 sec                                                                                                              | 2.02 sec: 1.04x faster                                                                                                    |
| connected_components    | 423 ms                                                                                                                | 410 ms: 1.03x faster                                                                                                      |
| bpe_tokeniser           | 4.71 sec                                                                                                              | 4.56 sec: 1.03x faster                                                                                                    |
| create_gc_cycles        | 2.93 ms                                                                                                               | 2.84 ms: 1.03x faster                                                                                                     |
| pickle_list             | 5.07 us                                                                                                               | 4.92 us: 1.03x faster                                                                                                     |
| scimark_fft             | 305 ms                                                                                                                | 298 ms: 1.02x faster                                                                                                      |
| pickle_dict             | 33.7 us                                                                                                               | 32.9 us: 1.02x faster                                                                                                     |
| coverage                | 82.7 ms                                                                                                               | 81.3 ms: 1.02x faster                                                                                                     |
| shortest_path           | 454 ms                                                                                                                | 447 ms: 1.02x faster                                                                                                      |
| json_dumps              | 10.2 ms                                                                                                               | 10.1 ms: 1.01x faster                                                                                                     |
| html5lib                | 67.3 ms                                                                                                               | 66.4 ms: 1.01x faster                                                                                                     |
| sqlite_synth            | 2.84 us                                                                                                               | 2.81 us: 1.01x faster                                                                                                     |
| pyflate                 | 406 ms                                                                                                                | 402 ms: 1.01x faster                                                                                                      |
| regex_dna               | 226 ms                                                                                                                | 224 ms: 1.01x faster                                                                                                      |
| asyncio_websockets      | 385 ms                                                                                                                | 381 ms: 1.01x faster                                                                                                      |
| logging_silent          | 92.8 ns                                                                                                               | 92.2 ns: 1.01x faster                                                                                                     |
| regex_effbot            | 3.56 ms                                                                                                               | 3.53 ms: 1.01x faster                                                                                                     |
| pickle_pure_python      | 325 us                                                                                                                | 326 us: 1.00x slower                                                                                                      |
| python_startup          | 15.3 ms                                                                                                               | 15.3 ms: 1.00x slower                                                                                                     |
| python_startup_no_site  | 8.80 ms                                                                                                               | 8.83 ms: 1.00x slower                                                                                                     |
| gc_traversal            | 6.43 ms                                                                                                               | 6.46 ms: 1.00x slower                                                                                                     |
| sympy_sum               | 150 ms                                                                                                                | 150 ms: 1.00x slower                                                                                                      |
| asyncio_tcp             | 368 ms                                                                                                                | 370 ms: 1.01x slower                                                                                                      |
| asyncio_tcp_ssl         | 1.58 sec                                                                                                              | 1.59 sec: 1.01x slower                                                                                                    |
| async_tree_none         | 268 ms                                                                                                                | 270 ms: 1.01x slower                                                                                                      |
| dulwich_log             | 58.5 ms                                                                                                               | 58.9 ms: 1.01x slower                                                                                                     |
| scimark_sor             | 101 ms                                                                                                                | 102 ms: 1.01x slower                                                                                                      |
| pathlib                 | 16.6 ms                                                                                                               | 16.7 ms: 1.01x slower                                                                                                     |
| docutils                | 2.87 sec                                                                                                              | 2.90 sec: 1.01x slower                                                                                                    |
| sqlglot_v2_transpile    | 1.68 ms                                                                                                               | 1.69 ms: 1.01x slower                                                                                                     |
| genshi_text             | 22.7 ms                                                                                                               | 22.9 ms: 1.01x slower                                                                                                     |
| many_optionals          | 1.21 ms                                                                                                               | 1.22 ms: 1.01x slower                                                                                                     |
| mdp                     | 1.27 sec                                                                                                              | 1.29 sec: 1.01x slower                                                                                                    |
| chaos                   | 58.1 ms                                                                                                               | 58.7 ms: 1.01x slower                                                                                                     |
| django_template         | 34.7 ms                                                                                                               | 35.1 ms: 1.01x slower                                                                                                     |
| subparsers              | 42.4 ms                                                                                                               | 43.0 ms: 1.01x slower                                                                                                     |
| telco                   | 157 ms                                                                                                                | 159 ms: 1.01x slower                                                                                                      |
| deepcopy_reduce         | 2.98 us                                                                                                               | 3.02 us: 1.01x slower                                                                                                     |
| 2to3                    | 281 ms                                                                                                                | 285 ms: 1.02x slower                                                                                                      |
| pickle                  | 12.1 us                                                                                                               | 12.3 us: 1.02x slower                                                                                                     |
| meteor_contest          | 121 ms                                                                                                                | 122 ms: 1.02x slower                                                                                                      |
| xml_etree_iterparse     | 96.8 ms                                                                                                               | 98.3 ms: 1.02x slower                                                                                                     |
| json                    | 5.36 ms                                                                                                               | 5.46 ms: 1.02x slower                                                                                                     |
| genshi_xml              | 52.9 ms                                                                                                               | 53.8 ms: 1.02x slower                                                                                                     |
| sympy_str               | 283 ms                                                                                                                | 289 ms: 1.02x slower                                                                                                      |
| regex_v8                | 23.4 ms                                                                                                               | 23.9 ms: 1.02x slower                                                                                                     |
| xml_etree_parse         | 137 ms                                                                                                                | 140 ms: 1.02x slower                                                                                                      |
| sympy_expand            | 486 ms                                                                                                                | 495 ms: 1.02x slower                                                                                                      |
| sympy_integrate         | 21.8 ms                                                                                                               | 22.2 ms: 1.02x slower                                                                                                     |
| logging_simple          | 5.84 us                                                                                                               | 5.96 us: 1.02x slower                                                                                                     |
| pylint                  | 318 ms                                                                                                                | 325 ms: 1.02x slower                                                                                                      |
| scimark_sparse_mat_mult | 4.92 ms                                                                                                               | 5.04 ms: 1.02x slower                                                                                                     |
| logging_format          | 6.36 us                                                                                                               | 6.52 us: 1.03x slower                                                                                                     |
| crypto_pyaes            | 74.8 ms                                                                                                               | 76.8 ms: 1.03x slower                                                                                                     |
| coroutines              | 22.0 ms                                                                                                               | 22.6 ms: 1.03x slower                                                                                                     |
| deepcopy_memo           | 27.7 us                                                                                                               | 28.5 us: 1.03x slower                                                                                                     |
| unpickle_list           | 4.97 us                                                                                                               | 5.11 us: 1.03x slower                                                                                                     |
| raytrace                | 276 ms                                                                                                                | 285 ms: 1.03x slower                                                                                                      |
| async_generators        | 421 ms                                                                                                                | 437 ms: 1.04x slower                                                                                                      |
| hexiom                  | 5.84 ms                                                                                                               | 6.09 ms: 1.04x slower                                                                                                     |
| sqlglot_v2_optimize     | 56.1 ms                                                                                                               | 58.6 ms: 1.05x slower                                                                                                     |
| fannkuch                | 361 ms                                                                                                                | 379 ms: 1.05x slower                                                                                                      |
| sqlglot_v2_normalize    | 111 ms                                                                                                                | 117 ms: 1.05x slower                                                                                                      |
| go                      | 117 ms                                                                                                                | 125 ms: 1.07x slower                                                                                                      |
| comprehensions          | 16.1 us                                                                                                               | 17.4 us: 1.08x slower                                                                                                     |
| nbody                   | 93.2 ms                                                                                                               | 104 ms: 1.11x slower                                                                                                      |
| scimark_monte_carlo     | 59.6 ms                                                                                                               | 66.6 ms: 1.12x slower                                                                                                     |
| unpack_sequence         | 43.1 ns                                                                                                               | 50.0 ns: 1.16x slower                                                                                                     |
| Geometric mean          | (ref)                                                                                                                 | 1.00x faster                                                                                                              |

Benchmark hidden because not significant (21): bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_io_tg, typing_runtime_protocols, async_tree_io, async_tree_none_tg, nqueens, json_loads, async_tree_memoization, sqlglot_v2_parse, scimark_lu, async_tree_cpu_io_mixed, djangocms, unpickle, regex_compile, pidigits, thrift, deepcopy, bench_thread_pool, async_tree_memoization_tg, sphinx

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 63.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x