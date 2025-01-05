# Results vs. base

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.037x faster
- HPT reliability: 99.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                                                                 | 220 ms: 1.02x faster                                                                                                       |
| docutils       | 1.65 sec                                                                                                               | 1.71 sec: 1.04x slower                                                                                                     |
| html5lib       | 39.4 ms                                                                                                                | 38.6 ms: 1.02x faster                                                                                                      |
| sphinx         | 645 ms                                                                                                                 | 674 ms: 1.04x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg         | 170 ms                                                                                                                 | 165 ms: 1.03x faster                                                                                                       |
| asyncio_websockets         | 315 ms                                                                                                                 | 306 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg           | 396 ms                                                                                                                 | 385 ms: 1.03x faster                                                                                                       |
| async_tree_memoization     | 222 ms                                                                                                                 | 217 ms: 1.03x faster                                                                                                       |
| async_tree_none            | 179 ms                                                                                                                 | 176 ms: 1.02x faster                                                                                                       |
| async_tree_io              | 397 ms                                                                                                                 | 392 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                                                                 | 339 ms: 1.01x faster                                                                                                       |
| async_generators           | 237 ms                                                                                                                 | 258 ms: 1.09x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.01x faster                                                                                                               |

Benchmark hidden because not significant (3): coroutines, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 75.3 ms                                                                                                                | 52.4 ms: 1.44x faster                                                                                                      |
| float          | 52.1 ms                                                                                                                | 40.3 ms: 1.29x faster                                                                                                      |
| pidigits       | 148 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.23x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 86.5 ms                                                                                                                | 79.7 ms: 1.09x faster                                                                                                      |
| regex_dna      | 116 ms                                                                                                                 | 120 ms: 1.03x slower                                                                                                       |
| regex_effbot   | 1.46 ms                                                                                                                | 1.53 ms: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                                                                                 | 108 us: 1.34x faster                                                                                                       |
| tomli_loads          | 1.39 sec                                                                                                               | 1.18 sec: 1.18x faster                                                                                                     |
| xml_etree_generate   | 56.4 ms                                                                                                                | 49.6 ms: 1.14x faster                                                                                                      |
| xml_etree_process    | 39.6 ms                                                                                                                | 35.7 ms: 1.11x faster                                                                                                      |
| pickle_pure_python   | 220 us                                                                                                                 | 205 us: 1.07x faster                                                                                                       |
| json_dumps           | 6.57 ms                                                                                                                | 6.23 ms: 1.06x faster                                                                                                      |
| xml_etree_iterparse  | 62.5 ms                                                                                                                | 59.3 ms: 1.05x faster                                                                                                      |
| xml_etree_parse      | 88.8 ms                                                                                                                | 86.1 ms: 1.03x faster                                                                                                      |
| json_loads           | 14.1 us                                                                                                                | 14.9 us: 1.05x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.10x faster                                                                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 17.3 ms                                                                                                                | 17.6 ms: 1.01x slower                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 6.69 ms                                                                                                                | 5.06 ms: 1.32x faster                                                                                                      |
| genshi_text     | 17.5 ms                                                                                                                | 18.7 ms: 1.07x slower                                                                                                      |
| django_template | 25.5 ms                                                                                                                | 27.5 ms: 1.08x slower                                                                                                      |
| genshi_xml      | 36.2 ms                                                                                                                | 48.0 ms: 1.32x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.04x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json | results/bm-20250104-3.14.0a3+-0cafa97-JIT/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 75.3 ms                                                                                                                | 52.4 ms: 1.44x faster                                                                                                      |
| scimark_sor                | 86.1 ms                                                                                                                | 62.8 ms: 1.37x faster                                                                                                      |
| unpickle_pure_python       | 145 us                                                                                                                 | 108 us: 1.34x faster                                                                                                       |
| scimark_fft                | 193 ms                                                                                                                 | 145 ms: 1.33x faster                                                                                                       |
| mako                       | 6.69 ms                                                                                                                | 5.06 ms: 1.32x faster                                                                                                      |
| float                      | 52.1 ms                                                                                                                | 40.3 ms: 1.29x faster                                                                                                      |
| scimark_monte_carlo        | 45.8 ms                                                                                                                | 36.7 ms: 1.25x faster                                                                                                      |
| scimark_sparse_mat_mult    | 2.59 ms                                                                                                                | 2.09 ms: 1.24x faster                                                                                                      |
| spectral_norm              | 62.2 ms                                                                                                                | 50.6 ms: 1.23x faster                                                                                                      |
| deepcopy_memo              | 19.8 us                                                                                                                | 16.2 us: 1.22x faster                                                                                                      |
| tomli_loads                | 1.39 sec                                                                                                               | 1.18 sec: 1.18x faster                                                                                                     |
| crypto_pyaes               | 48.1 ms                                                                                                                | 41.3 ms: 1.17x faster                                                                                                      |
| xml_etree_generate         | 56.4 ms                                                                                                                | 49.6 ms: 1.14x faster                                                                                                      |
| bpe_tokeniser              | 3.00 sec                                                                                                               | 2.65 sec: 1.13x faster                                                                                                     |
| pyflate                    | 321 ms                                                                                                                 | 283 ms: 1.13x faster                                                                                                       |
| scimark_lu                 | 60.5 ms                                                                                                                | 53.5 ms: 1.13x faster                                                                                                      |
| telco                      | 4.76 ms                                                                                                                | 4.24 ms: 1.12x faster                                                                                                      |
| xml_etree_process          | 39.6 ms                                                                                                                | 35.7 ms: 1.11x faster                                                                                                      |
| pprint_safe_repr           | 531 ms                                                                                                                 | 483 ms: 1.10x faster                                                                                                       |
| pprint_pformat             | 1.07 sec                                                                                                               | 972 ms: 1.10x faster                                                                                                       |
| logging_silent             | 61.6 ns                                                                                                                | 56.5 ns: 1.09x faster                                                                                                      |
| regex_compile              | 86.5 ms                                                                                                                | 79.7 ms: 1.09x faster                                                                                                      |
| fannkuch                   | 270 ms                                                                                                                 | 252 ms: 1.07x faster                                                                                                       |
| pickle_pure_python         | 220 us                                                                                                                 | 205 us: 1.07x faster                                                                                                       |
| sqlglot_parse              | 895 us                                                                                                                 | 838 us: 1.07x faster                                                                                                       |
| dulwich_log                | 42.1 ms                                                                                                                | 39.8 ms: 1.06x faster                                                                                                      |
| k_core                     | 1.68 sec                                                                                                               | 1.59 sec: 1.06x faster                                                                                                     |
| json_dumps                 | 6.57 ms                                                                                                                | 6.23 ms: 1.06x faster                                                                                                      |
| xml_etree_iterparse        | 62.5 ms                                                                                                                | 59.3 ms: 1.05x faster                                                                                                      |
| chaos                      | 43.0 ms                                                                                                                | 41.1 ms: 1.05x faster                                                                                                      |
| connected_components       | 322 ms                                                                                                                 | 310 ms: 1.04x faster                                                                                                       |
| meteor_contest             | 76.9 ms                                                                                                                | 74.4 ms: 1.03x faster                                                                                                      |
| sqlite_synth               | 1.61 us                                                                                                                | 1.55 us: 1.03x faster                                                                                                      |
| logging_format             | 6.86 us                                                                                                                | 6.65 us: 1.03x faster                                                                                                      |
| xml_etree_parse            | 88.8 ms                                                                                                                | 86.1 ms: 1.03x faster                                                                                                      |
| async_tree_none_tg         | 170 ms                                                                                                                 | 165 ms: 1.03x faster                                                                                                       |
| sqlglot_transpile          | 1.11 ms                                                                                                                | 1.08 ms: 1.03x faster                                                                                                      |
| asyncio_websockets         | 315 ms                                                                                                                 | 306 ms: 1.03x faster                                                                                                       |
| async_tree_io_tg           | 396 ms                                                                                                                 | 385 ms: 1.03x faster                                                                                                       |
| json                       | 2.98 ms                                                                                                                | 2.90 ms: 1.03x faster                                                                                                      |
| async_tree_memoization     | 222 ms                                                                                                                 | 217 ms: 1.03x faster                                                                                                       |
| html5lib                   | 39.4 ms                                                                                                                | 38.6 ms: 1.02x faster                                                                                                      |
| async_tree_none            | 179 ms                                                                                                                 | 176 ms: 1.02x faster                                                                                                       |
| 2to3                       | 224 ms                                                                                                                 | 220 ms: 1.02x faster                                                                                                       |
| logging_simple             | 6.36 us                                                                                                                | 6.25 us: 1.02x faster                                                                                                      |
| shortest_path              | 351 ms                                                                                                                 | 345 ms: 1.02x faster                                                                                                       |
| async_tree_io              | 397 ms                                                                                                                 | 392 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 343 ms                                                                                                                 | 339 ms: 1.01x faster                                                                                                       |
| subparsers                 | 16.0 ms                                                                                                                | 15.8 ms: 1.01x faster                                                                                                      |
| typing_runtime_protocols   | 113 us                                                                                                                 | 112 us: 1.01x faster                                                                                                       |
| pidigits                   | 148 ms                                                                                                                 | 147 ms: 1.01x faster                                                                                                       |
| sympy_expand               | 306 ms                                                                                                                 | 305 ms: 1.00x faster                                                                                                       |
| deltablue                  | 2.25 ms                                                                                                                | 2.27 ms: 1.01x slower                                                                                                      |
| create_gc_cycles           | 1.20 ms                                                                                                                | 1.22 ms: 1.01x slower                                                                                                      |
| mypy2                      | 637 ms                                                                                                                 | 646 ms: 1.01x slower                                                                                                       |
| python_startup_no_site     | 17.3 ms                                                                                                                | 17.6 ms: 1.01x slower                                                                                                      |
| sympy_integrate            | 13.3 ms                                                                                                                | 13.5 ms: 1.01x slower                                                                                                      |
| sympy_sum                  | 89.9 ms                                                                                                                | 91.2 ms: 1.02x slower                                                                                                      |
| deepcopy                   | 185 us                                                                                                                 | 190 us: 1.03x slower                                                                                                       |
| regex_dna                  | 116 ms                                                                                                                 | 120 ms: 1.03x slower                                                                                                       |
| coverage                   | 45.8 ms                                                                                                                | 47.1 ms: 1.03x slower                                                                                                      |
| many_optionals             | 443 us                                                                                                                 | 457 us: 1.03x slower                                                                                                       |
| go                         | 87.1 ms                                                                                                                | 89.9 ms: 1.03x slower                                                                                                      |
| docutils                   | 1.65 sec                                                                                                               | 1.71 sec: 1.04x slower                                                                                                     |
| sphinx                     | 645 ms                                                                                                                 | 674 ms: 1.04x slower                                                                                                       |
| sqlglot_optimize           | 35.9 ms                                                                                                                | 37.5 ms: 1.05x slower                                                                                                      |
| regex_effbot               | 1.46 ms                                                                                                                | 1.53 ms: 1.05x slower                                                                                                      |
| mdp                        | 1.46 sec                                                                                                               | 1.53 sec: 1.05x slower                                                                                                     |
| sqlglot_normalize          | 195 ms                                                                                                                 | 205 ms: 1.05x slower                                                                                                       |
| json_loads                 | 14.1 us                                                                                                                | 14.9 us: 1.05x slower                                                                                                      |
| pylint                     | 198 ms                                                                                                                 | 210 ms: 1.06x slower                                                                                                       |
| raytrace                   | 190 ms                                                                                                                 | 202 ms: 1.07x slower                                                                                                       |
| genshi_text                | 17.5 ms                                                                                                                | 18.7 ms: 1.07x slower                                                                                                      |
| django_template            | 25.5 ms                                                                                                                | 27.5 ms: 1.08x slower                                                                                                      |
| async_generators           | 237 ms                                                                                                                 | 258 ms: 1.09x slower                                                                                                       |
| richards_super             | 34.5 ms                                                                                                                | 37.7 ms: 1.09x slower                                                                                                      |
| generators                 | 21.2 ms                                                                                                                | 23.2 ms: 1.10x slower                                                                                                      |
| richards                   | 30.4 ms                                                                                                                | 33.4 ms: 1.10x slower                                                                                                      |
| hexiom                     | 4.34 ms                                                                                                                | 5.00 ms: 1.15x slower                                                                                                      |
| genshi_xml                 | 36.2 ms                                                                                                                | 48.0 ms: 1.32x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmark hidden because not significant (15): pycparser, bench_thread_pool, thrift, coroutines, nqueens, python_startup, deepcopy_reduce, sympy_str, gc_traversal, async_tree_memoization_tg, async_tree_cpu_io_mixed, comprehensions, bench_mp_pool, pathlib, regex_v8

- Geometric mean (including insignificant results): 1.037x faster

# HPT report

- Reliability score: 99.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown