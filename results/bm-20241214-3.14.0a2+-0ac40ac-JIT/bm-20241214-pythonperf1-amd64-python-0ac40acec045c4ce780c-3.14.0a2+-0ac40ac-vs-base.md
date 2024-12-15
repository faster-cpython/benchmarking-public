# Results vs. base

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-amd64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.048x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                                                                 | 219 ms: 1.02x faster                                                                                                       |
| docutils       | 1.66 sec                                                                                                               | 1.72 sec: 1.04x slower                                                                                                     |
| html5lib       | 40.6 ms                                                                                                                | 39.2 ms: 1.03x faster                                                                                                      |
| sphinx         | 652 ms                                                                                                                 | 671 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg      | 175 ms                                                                                                                 | 170 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg        | 411 ms                                                                                                                 | 400 ms: 1.03x faster                                                                                                       |
| async_tree_io           | 415 ms                                                                                                                 | 405 ms: 1.03x faster                                                                                                       |
| async_tree_memoization  | 227 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| coroutines              | 13.4 ms                                                                                                                | 13.3 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed | 356 ms                                                                                                                 | 362 ms: 1.01x slower                                                                                                       |
| async_generators        | 238 ms                                                                                                                 | 249 ms: 1.04x slower                                                                                                       |
| Geometric mean          | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 79.5 ms                                                                                                                | 54.6 ms: 1.46x faster                                                                                                      |
| float          | 54.4 ms                                                                                                                | 43.8 ms: 1.24x faster                                                                                                      |
| pidigits       | 148 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.22x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 89.2 ms                                                                                                                | 79.6 ms: 1.12x faster                                                                                                      |
| regex_effbot   | 1.40 ms                                                                                                                | 1.45 ms: 1.04x slower                                                                                                      |
| regex_dna      | 111 ms                                                                                                                 | 116 ms: 1.05x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.03x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 147 us                                                                                                                 | 112 us: 1.32x faster                                                                                                       |
| tomli_loads          | 1.54 sec                                                                                                               | 1.21 sec: 1.27x faster                                                                                                     |
| xml_etree_process    | 41.3 ms                                                                                                                | 35.3 ms: 1.17x faster                                                                                                      |
| xml_etree_generate   | 57.5 ms                                                                                                                | 49.9 ms: 1.15x faster                                                                                                      |
| pickle_pure_python   | 222 us                                                                                                                 | 205 us: 1.08x faster                                                                                                       |
| json_dumps           | 6.73 ms                                                                                                                | 6.30 ms: 1.07x faster                                                                                                      |
| xml_etree_iterparse  | 63.0 ms                                                                                                                | 59.1 ms: 1.07x faster                                                                                                      |
| xml_etree_parse      | 87.8 ms                                                                                                                | 86.4 ms: 1.02x faster                                                                                                      |
| json_loads           | 14.4 us                                                                                                                | 14.2 us: 1.01x faster                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.12x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.76 ms                                                                                                                | 5.04 ms: 1.34x faster                                                                                                      |
| genshi_text     | 17.2 ms                                                                                                                | 18.5 ms: 1.07x slower                                                                                                      |
| django_template | 24.9 ms                                                                                                                | 27.0 ms: 1.08x slower                                                                                                      |
| genshi_xml      | 37.1 ms                                                                                                                | 46.9 ms: 1.26x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.02x slower                                                                                                               |

All benchmarks:
===============

| Benchmark               | results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json | results/bm-20241214-3.14.0a2+-0ac40ac-JIT/bm-20241214-pythonperf1-amd64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json |
|-------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                   | 79.5 ms                                                                                                                | 54.6 ms: 1.46x faster                                                                                                      |
| scimark_sor             | 87.1 ms                                                                                                                | 62.6 ms: 1.39x faster                                                                                                      |
| mako                    | 6.76 ms                                                                                                                | 5.04 ms: 1.34x faster                                                                                                      |
| scimark_fft             | 189 ms                                                                                                                 | 142 ms: 1.33x faster                                                                                                       |
| spectral_norm           | 62.0 ms                                                                                                                | 46.9 ms: 1.32x faster                                                                                                      |
| unpickle_pure_python    | 147 us                                                                                                                 | 112 us: 1.32x faster                                                                                                       |
| scimark_monte_carlo     | 47.2 ms                                                                                                                | 35.8 ms: 1.32x faster                                                                                                      |
| deepcopy_memo           | 21.1 us                                                                                                                | 16.1 us: 1.31x faster                                                                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                                                                                | 2.00 ms: 1.28x faster                                                                                                      |
| tomli_loads             | 1.54 sec                                                                                                               | 1.21 sec: 1.27x faster                                                                                                     |
| float                   | 54.4 ms                                                                                                                | 43.8 ms: 1.24x faster                                                                                                      |
| crypto_pyaes            | 49.4 ms                                                                                                                | 41.0 ms: 1.20x faster                                                                                                      |
| xml_etree_process       | 41.3 ms                                                                                                                | 35.3 ms: 1.17x faster                                                                                                      |
| pprint_pformat          | 1.11 sec                                                                                                               | 962 ms: 1.16x faster                                                                                                       |
| xml_etree_generate      | 57.5 ms                                                                                                                | 49.9 ms: 1.15x faster                                                                                                      |
| pprint_safe_repr        | 556 ms                                                                                                                 | 489 ms: 1.14x faster                                                                                                       |
| bpe_tokeniser           | 2.97 sec                                                                                                               | 2.62 sec: 1.13x faster                                                                                                     |
| regex_compile           | 89.2 ms                                                                                                                | 79.6 ms: 1.12x faster                                                                                                      |
| logging_silent          | 60.8 ns                                                                                                                | 54.8 ns: 1.11x faster                                                                                                      |
| pyflate                 | 313 ms                                                                                                                 | 282 ms: 1.11x faster                                                                                                       |
| telco                   | 4.76 ms                                                                                                                | 4.34 ms: 1.10x faster                                                                                                      |
| scimark_lu              | 61.5 ms                                                                                                                | 56.8 ms: 1.08x faster                                                                                                      |
| pickle_pure_python      | 222 us                                                                                                                 | 205 us: 1.08x faster                                                                                                       |
| k_core                  | 1.69 sec                                                                                                               | 1.57 sec: 1.07x faster                                                                                                     |
| coverage                | 48.0 ms                                                                                                                | 44.7 ms: 1.07x faster                                                                                                      |
| fannkuch                | 271 ms                                                                                                                 | 253 ms: 1.07x faster                                                                                                       |
| sqlglot_parse           | 891 us                                                                                                                 | 833 us: 1.07x faster                                                                                                       |
| json_dumps              | 6.73 ms                                                                                                                | 6.30 ms: 1.07x faster                                                                                                      |
| xml_etree_iterparse     | 63.0 ms                                                                                                                | 59.1 ms: 1.07x faster                                                                                                      |
| chaos                   | 43.9 ms                                                                                                                | 41.5 ms: 1.06x faster                                                                                                      |
| connected_components    | 327 ms                                                                                                                 | 310 ms: 1.06x faster                                                                                                       |
| dulwich_log             | 42.9 ms                                                                                                                | 40.6 ms: 1.06x faster                                                                                                      |
| deepcopy_reduce         | 1.92 us                                                                                                                | 1.83 us: 1.05x faster                                                                                                      |
| shortest_path           | 360 ms                                                                                                                 | 344 ms: 1.05x faster                                                                                                       |
| json                    | 2.96 ms                                                                                                                | 2.84 ms: 1.04x faster                                                                                                      |
| html5lib                | 40.6 ms                                                                                                                | 39.2 ms: 1.03x faster                                                                                                      |
| sqlglot_transpile       | 1.11 ms                                                                                                                | 1.07 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg      | 175 ms                                                                                                                 | 170 ms: 1.03x faster                                                                                                       |
| sqlite_synth            | 1.61 us                                                                                                                | 1.56 us: 1.03x faster                                                                                                      |
| meteor_contest          | 77.5 ms                                                                                                                | 75.1 ms: 1.03x faster                                                                                                      |
| async_tree_io_tg        | 411 ms                                                                                                                 | 400 ms: 1.03x faster                                                                                                       |
| async_tree_io           | 415 ms                                                                                                                 | 405 ms: 1.03x faster                                                                                                       |
| logging_format          | 6.86 us                                                                                                                | 6.70 us: 1.02x faster                                                                                                      |
| logging_simple          | 6.42 us                                                                                                                | 6.29 us: 1.02x faster                                                                                                      |
| pycparser               | 737 ms                                                                                                                 | 722 ms: 1.02x faster                                                                                                       |
| xml_etree_parse         | 87.8 ms                                                                                                                | 86.4 ms: 1.02x faster                                                                                                      |
| 2to3                    | 223 ms                                                                                                                 | 219 ms: 1.02x faster                                                                                                       |
| async_tree_memoization  | 227 ms                                                                                                                 | 224 ms: 1.02x faster                                                                                                       |
| coroutines              | 13.4 ms                                                                                                                | 13.3 ms: 1.01x faster                                                                                                      |
| thrift                  | 522 us                                                                                                                 | 516 us: 1.01x faster                                                                                                       |
| json_loads              | 14.4 us                                                                                                                | 14.2 us: 1.01x faster                                                                                                      |
| comprehensions          | 12.0 us                                                                                                                | 11.8 us: 1.01x faster                                                                                                      |
| pidigits                | 148 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| sympy_str               | 176 ms                                                                                                                 | 175 ms: 1.00x faster                                                                                                       |
| sympy_expand            | 302 ms                                                                                                                 | 301 ms: 1.00x faster                                                                                                       |
| sympy_integrate         | 13.3 ms                                                                                                                | 13.5 ms: 1.01x slower                                                                                                      |
| sympy_sum               | 89.2 ms                                                                                                                | 90.5 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed | 356 ms                                                                                                                 | 362 ms: 1.01x slower                                                                                                       |
| nqueens                 | 62.8 ms                                                                                                                | 64.0 ms: 1.02x slower                                                                                                      |
| many_optionals          | 441 us                                                                                                                 | 453 us: 1.03x slower                                                                                                       |
| generators              | 22.2 ms                                                                                                                | 22.8 ms: 1.03x slower                                                                                                      |
| sphinx                  | 652 ms                                                                                                                 | 671 ms: 1.03x slower                                                                                                       |
| sqlglot_normalize       | 195 ms                                                                                                                 | 202 ms: 1.04x slower                                                                                                       |
| regex_effbot            | 1.40 ms                                                                                                                | 1.45 ms: 1.04x slower                                                                                                      |
| sqlglot_optimize        | 35.9 ms                                                                                                                | 37.2 ms: 1.04x slower                                                                                                      |
| docutils                | 1.66 sec                                                                                                               | 1.72 sec: 1.04x slower                                                                                                     |
| async_generators        | 238 ms                                                                                                                 | 249 ms: 1.04x slower                                                                                                       |
| pylint                  | 198 ms                                                                                                                 | 207 ms: 1.04x slower                                                                                                       |
| regex_dna               | 111 ms                                                                                                                 | 116 ms: 1.05x slower                                                                                                       |
| richards_super          | 36.2 ms                                                                                                                | 38.0 ms: 1.05x slower                                                                                                      |
| richards                | 32.0 ms                                                                                                                | 33.7 ms: 1.05x slower                                                                                                      |
| genshi_text             | 17.2 ms                                                                                                                | 18.5 ms: 1.07x slower                                                                                                      |
| django_template         | 24.9 ms                                                                                                                | 27.0 ms: 1.08x slower                                                                                                      |
| mdp                     | 1.43 sec                                                                                                               | 1.55 sec: 1.08x slower                                                                                                     |
| raytrace                | 191 ms                                                                                                                 | 209 ms: 1.09x slower                                                                                                       |
| hexiom                  | 4.31 ms                                                                                                                | 4.95 ms: 1.15x slower                                                                                                      |
| genshi_xml              | 37.1 ms                                                                                                                | 46.9 ms: 1.26x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (18): regex_v8, asyncio_websockets, python_startup_no_site, bench_thread_pool, async_tree_cpu_io_mixed_tg, deepcopy, gc_traversal, mypy2, create_gc_cycles, pathlib, subparsers, async_tree_memoization_tg, typing_runtime_protocols, go, deltablue, async_tree_none, bench_mp_pool, python_startup

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown