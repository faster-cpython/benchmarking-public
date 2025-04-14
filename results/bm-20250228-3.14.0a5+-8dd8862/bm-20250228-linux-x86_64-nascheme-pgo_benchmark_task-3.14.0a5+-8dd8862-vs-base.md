# Results vs. base

- fork: nascheme
- ref: pgo_benchmark_task
- machine: linux-x86_64
- commit hash: 8dd8862
- commit date: 2025-02-28
- overall geometric mean: 1.013x faster
- HPT reliability: 92.07%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 258 ms: 1.02x slower                                                   |
| docutils       | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                 |
| html5lib       | 62.1 ms                                                                | 61.3 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                 | 24.1 ms                                                                | 22.3 ms: 1.08x faster                                                  |
| async_generators           | 383 ms                                                                 | 365 ms: 1.05x faster                                                   |
| async_tree_none            | 258 ms                                                                 | 248 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 250 ms                                                                 | 240 ms: 1.04x faster                                                   |
| async_tree_memoization_tg  | 316 ms                                                                 | 305 ms: 1.04x faster                                                   |
| async_tree_memoization     | 316 ms                                                                 | 306 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 459 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 481 ms                                                                 | 468 ms: 1.03x faster                                                   |
| async_tree_io              | 606 ms                                                                 | 593 ms: 1.02x faster                                                   |
| Geometric mean             | (ref)                                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 70.5 ms                                                                | 69.7 ms: 1.01x faster                                                  |
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 94.9 ms                                                                | 96.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 214 ms                                                                 | 188 ms: 1.14x faster                                                   |
| regex_v8       | 24.7 ms                                                                | 22.9 ms: 1.08x faster                                                  |
| regex_compile  | 125 ms                                                                 | 129 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 146 ms                                                                 | 129 ms: 1.13x faster                                                   |
| json_loads           | 30.2 us                                                                | 26.7 us: 1.13x faster                                                  |
| xml_etree_iterparse  | 99.5 ms                                                                | 93.9 ms: 1.06x faster                                                  |
| json_dumps           | 11.2 ms                                                                | 10.7 ms: 1.05x faster                                                  |
| xml_etree_generate   | 82.8 ms                                                                | 80.4 ms: 1.03x faster                                                  |
| xml_etree_process    | 57.6 ms                                                                | 56.5 ms: 1.02x faster                                                  |
| pickle_pure_python   | 320 us                                                                 | 316 us: 1.01x faster                                                   |
| tomli_loads          | 2.01 sec                                                               | 2.02 sec: 1.01x slower                                                 |
| unpickle_pure_python | 219 us                                                                 | 227 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 7.16 ms                                                                | 7.18 ms: 1.00x slower                                                  |
| python_startup         | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| mako            | 11.3 ms                                                                | 11.6 ms: 1.03x slower                                                  |
| genshi_text     | 21.5 ms                                                                | 22.3 ms: 1.04x slower                                                  |
| genshi_xml      | 49.0 ms                                                                | 50.9 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250226-linux-x86_64-python-9e474a98af4184615540-3.14.0a5+-9e474a9 | bm-20250228-linux-x86_64-nascheme-pgo_benchmark_task-3.14.0a5+-8dd8862 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| telco                      | 7.78 ms                                                                | 6.81 ms: 1.14x faster                                                  |
| regex_dna                  | 214 ms                                                                 | 188 ms: 1.14x faster                                                   |
| xml_etree_parse            | 146 ms                                                                 | 129 ms: 1.13x faster                                                   |
| json_loads                 | 30.2 us                                                                | 26.7 us: 1.13x faster                                                  |
| fannkuch                   | 407 ms                                                                 | 364 ms: 1.12x faster                                                   |
| spectral_norm              | 99.1 ms                                                                | 91.1 ms: 1.09x faster                                                  |
| regex_v8                   | 24.7 ms                                                                | 22.9 ms: 1.08x faster                                                  |
| coroutines                 | 24.1 ms                                                                | 22.3 ms: 1.08x faster                                                  |
| scimark_fft                | 347 ms                                                                 | 323 ms: 1.08x faster                                                   |
| meteor_contest             | 105 ms                                                                 | 98.2 ms: 1.07x faster                                                  |
| scimark_monte_carlo        | 68.2 ms                                                                | 64.2 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 99.5 ms                                                                | 93.9 ms: 1.06x faster                                                  |
| deepcopy_reduce            | 2.77 us                                                                | 2.63 us: 1.05x faster                                                  |
| async_generators           | 383 ms                                                                 | 365 ms: 1.05x faster                                                   |
| json_dumps                 | 11.2 ms                                                                | 10.7 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult    | 4.88 ms                                                                | 4.66 ms: 1.05x faster                                                  |
| async_tree_none            | 258 ms                                                                 | 248 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 250 ms                                                                 | 240 ms: 1.04x faster                                                   |
| async_tree_memoization_tg  | 316 ms                                                                 | 305 ms: 1.04x faster                                                   |
| pyflate                    | 451 ms                                                                 | 435 ms: 1.04x faster                                                   |
| async_tree_memoization     | 316 ms                                                                 | 306 ms: 1.03x faster                                                   |
| deepcopy                   | 259 us                                                                 | 250 us: 1.03x faster                                                   |
| typing_runtime_protocols   | 159 us                                                                 | 154 us: 1.03x faster                                                   |
| logging_silent             | 108 ns                                                                 | 105 ns: 1.03x faster                                                   |
| xml_etree_generate         | 82.8 ms                                                                | 80.4 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 473 ms                                                                 | 459 ms: 1.03x faster                                                   |
| richards_super             | 50.1 ms                                                                | 48.8 ms: 1.03x faster                                                  |
| hexiom                     | 6.17 ms                                                                | 6.01 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 481 ms                                                                 | 468 ms: 1.03x faster                                                   |
| scimark_sor                | 121 ms                                                                 | 118 ms: 1.03x faster                                                   |
| richards                   | 43.8 ms                                                                | 42.8 ms: 1.02x faster                                                  |
| async_tree_io              | 606 ms                                                                 | 593 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 715 ms                                                                 | 700 ms: 1.02x faster                                                   |
| xml_etree_process          | 57.6 ms                                                                | 56.5 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.47 sec                                                               | 1.44 sec: 1.02x faster                                                 |
| chaos                      | 58.7 ms                                                                | 57.6 ms: 1.02x faster                                                  |
| json                       | 5.37 ms                                                                | 5.29 ms: 1.02x faster                                                  |
| deepcopy_memo              | 30.2 us                                                                | 29.8 us: 1.02x faster                                                  |
| pickle_pure_python         | 320 us                                                                 | 316 us: 1.01x faster                                                   |
| html5lib                   | 62.1 ms                                                                | 61.3 ms: 1.01x faster                                                  |
| float                      | 70.5 ms                                                                | 69.7 ms: 1.01x faster                                                  |
| nqueens                    | 80.1 ms                                                                | 79.4 ms: 1.01x faster                                                  |
| gc_traversal               | 4.86 ms                                                                | 4.83 ms: 1.01x faster                                                  |
| bpe_tokeniser              | 4.46 sec                                                               | 4.43 sec: 1.01x faster                                                 |
| comprehensions             | 16.4 us                                                                | 16.3 us: 1.01x faster                                                  |
| logging_format             | 6.12 us                                                                | 6.08 us: 1.01x faster                                                  |
| docutils                   | 2.60 sec                                                               | 2.59 sec: 1.00x faster                                                 |
| pidigits                   | 186 ms                                                                 | 186 ms: 1.00x faster                                                   |
| python_startup_no_site     | 7.16 ms                                                                | 7.18 ms: 1.00x slower                                                  |
| scimark_lu                 | 116 ms                                                                 | 116 ms: 1.01x slower                                                   |
| mdp                        | 2.49 sec                                                               | 2.50 sec: 1.01x slower                                                 |
| bench_mp_pool              | 82.1 ms                                                                | 82.6 ms: 1.01x slower                                                  |
| python_startup             | 13.0 ms                                                                | 13.1 ms: 1.01x slower                                                  |
| tomli_loads                | 2.01 sec                                                               | 2.02 sec: 1.01x slower                                                 |
| go                         | 116 ms                                                                 | 117 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.46 ms                                                                | 2.48 ms: 1.01x slower                                                  |
| many_optionals             | 931 us                                                                 | 942 us: 1.01x slower                                                   |
| bench_thread_pool          | 868 us                                                                 | 880 us: 1.01x slower                                                   |
| sqlalchemy_declarative     | 128 ms                                                                 | 130 ms: 1.01x slower                                                   |
| connected_components       | 433 ms                                                                 | 440 ms: 1.02x slower                                                   |
| crypto_pyaes               | 72.3 ms                                                                | 73.7 ms: 1.02x slower                                                  |
| 2to3                       | 253 ms                                                                 | 258 ms: 1.02x slower                                                   |
| nbody                      | 94.9 ms                                                                | 96.8 ms: 1.02x slower                                                  |
| django_template            | 31.6 ms                                                                | 32.2 ms: 1.02x slower                                                  |
| sympy_integrate            | 19.7 ms                                                                | 20.2 ms: 1.02x slower                                                  |
| sqlalchemy_imperative      | 16.4 ms                                                                | 16.8 ms: 1.02x slower                                                  |
| mako                       | 11.3 ms                                                                | 11.6 ms: 1.03x slower                                                  |
| sympy_expand               | 454 ms                                                                 | 466 ms: 1.03x slower                                                   |
| sympy_str                  | 267 ms                                                                 | 274 ms: 1.03x slower                                                   |
| regex_compile              | 125 ms                                                                 | 129 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 104 ms                                                                 | 107 ms: 1.03x slower                                                   |
| sqlglot_optimize           | 52.2 ms                                                                | 53.7 ms: 1.03x slower                                                  |
| dulwich_log                | 64.9 ms                                                                | 66.9 ms: 1.03x slower                                                  |
| sympy_sum                  | 147 ms                                                                 | 152 ms: 1.03x slower                                                   |
| unpickle_pure_python       | 219 us                                                                 | 227 us: 1.04x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                                | 1.63 ms: 1.04x slower                                                  |
| genshi_text                | 21.5 ms                                                                | 22.3 ms: 1.04x slower                                                  |
| sqlglot_parse              | 1.26 ms                                                                | 1.31 ms: 1.04x slower                                                  |
| genshi_xml                 | 49.0 ms                                                                | 50.9 ms: 1.04x slower                                                  |
| pycparser                  | 1.11 sec                                                               | 1.16 sec: 1.04x slower                                                 |
| coverage                   | 84.1 ms                                                                | 88.7 ms: 1.05x slower                                                  |
| thrift                     | 769 us                                                                 | 817 us: 1.06x slower                                                   |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (14): async_tree_io_tg, sqlite_synth, generators, raytrace, subparsers, asyncio_websockets, k_core, regex_effbot, sphinx, pathlib, deltablue, shortest_path, logging_simple, pylint

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 92.07% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x