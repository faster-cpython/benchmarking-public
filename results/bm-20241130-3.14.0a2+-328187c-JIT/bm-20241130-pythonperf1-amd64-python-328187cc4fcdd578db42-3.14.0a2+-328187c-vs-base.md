# Results vs. base

- fork: python
- ref: 328187cc4fcdd578db42
- machine: windows-amd64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.053x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| docutils       | 1.69 sec                                                                                                               | 1.80 sec: 1.06x slower                                                                                                     |
| html5lib       | 40.9 ms                                                                                                                | 38.7 ms: 1.06x faster                                                                                                      |
| sphinx         | 673 ms                                                                                                                 | 694 ms: 1.03x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_memoization     | 276 ms                                                                                                                 | 273 ms: 1.01x faster                                                                                                       |
| async_tree_cpu_io_mixed_tg | 419 ms                                                                                                                 | 414 ms: 1.01x faster                                                                                                       |
| asyncio_websockets         | 301 ms                                                                                                                 | 314 ms: 1.04x slower                                                                                                       |
| async_generators           | 248 ms                                                                                                                 | 266 ms: 1.07x slower                                                                                                       |
| Geometric mean             | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (7): async_tree_none, async_tree_io_tg, async_tree_none_tg, coroutines, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 79.3 ms                                                                                                                | 50.8 ms: 1.56x faster                                                                                                      |
| float          | 56.6 ms                                                                                                                | 47.7 ms: 1.19x faster                                                                                                      |
| Geometric mean | (ref)                                                                                                                  | 1.23x faster                                                                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 91.5 ms                                                                                                                | 85.2 ms: 1.07x faster                                                                                                      |
| regex_v8       | 15.4 ms                                                                                                                | 14.8 ms: 1.04x faster                                                                                                      |
| regex_effbot   | 1.44 ms                                                                                                                | 1.41 ms: 1.02x faster                                                                                                      |
| regex_dna      | 116 ms                                                                                                                 | 113 ms: 1.02x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 155 us                                                                                                                 | 108 us: 1.43x faster                                                                                                       |
| tomli_loads          | 1.58 sec                                                                                                               | 1.28 sec: 1.24x faster                                                                                                     |
| xml_etree_process    | 41.2 ms                                                                                                                | 36.6 ms: 1.13x faster                                                                                                      |
| xml_etree_generate   | 58.2 ms                                                                                                                | 52.5 ms: 1.11x faster                                                                                                      |
| json_dumps           | 7.08 ms                                                                                                                | 6.45 ms: 1.10x faster                                                                                                      |
| pickle_pure_python   | 227 us                                                                                                                 | 207 us: 1.10x faster                                                                                                       |
| xml_etree_iterparse  | 65.5 ms                                                                                                                | 63.6 ms: 1.03x faster                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.12x faster                                                                                                               |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.53 ms                                                                                                                | 5.19 ms: 1.45x faster                                                                                                      |
| django_template | 25.3 ms                                                                                                                | 26.6 ms: 1.05x slower                                                                                                      |
| genshi_text     | 16.9 ms                                                                                                                | 18.7 ms: 1.11x slower                                                                                                      |
| genshi_xml      | 35.8 ms                                                                                                                | 43.9 ms: 1.22x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.00x faster                                                                                                               |

All benchmarks:
===============

| Benchmark                  | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf1-amd64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                      | 79.3 ms                                                                                                                | 50.8 ms: 1.56x faster                                                                                                      |
| mako                       | 7.53 ms                                                                                                                | 5.19 ms: 1.45x faster                                                                                                      |
| unpickle_pure_python       | 155 us                                                                                                                 | 108 us: 1.43x faster                                                                                                       |
| scimark_sor                | 91.6 ms                                                                                                                | 64.4 ms: 1.42x faster                                                                                                      |
| scimark_monte_carlo        | 48.8 ms                                                                                                                | 36.1 ms: 1.35x faster                                                                                                      |
| deepcopy_memo              | 21.3 us                                                                                                                | 16.1 us: 1.32x faster                                                                                                      |
| spectral_norm              | 72.7 ms                                                                                                                | 55.4 ms: 1.31x faster                                                                                                      |
| scimark_fft                | 206 ms                                                                                                                 | 157 ms: 1.31x faster                                                                                                       |
| scimark_sparse_mat_mult    | 2.80 ms                                                                                                                | 2.23 ms: 1.26x faster                                                                                                      |
| tomli_loads                | 1.58 sec                                                                                                               | 1.28 sec: 1.24x faster                                                                                                     |
| scimark_lu                 | 63.4 ms                                                                                                                | 52.2 ms: 1.21x faster                                                                                                      |
| crypto_pyaes               | 49.1 ms                                                                                                                | 40.5 ms: 1.21x faster                                                                                                      |
| float                      | 56.6 ms                                                                                                                | 47.7 ms: 1.19x faster                                                                                                      |
| pprint_safe_repr           | 556 ms                                                                                                                 | 472 ms: 1.18x faster                                                                                                       |
| pprint_pformat             | 1.12 sec                                                                                                               | 958 ms: 1.17x faster                                                                                                       |
| logging_silent             | 67.4 ns                                                                                                                | 58.0 ns: 1.16x faster                                                                                                      |
| pyflate                    | 327 ms                                                                                                                 | 285 ms: 1.15x faster                                                                                                       |
| bpe_tokeniser              | 3.10 sec                                                                                                               | 2.71 sec: 1.14x faster                                                                                                     |
| fannkuch                   | 292 ms                                                                                                                 | 257 ms: 1.13x faster                                                                                                       |
| xml_etree_process          | 41.2 ms                                                                                                                | 36.6 ms: 1.13x faster                                                                                                      |
| telco                      | 4.88 ms                                                                                                                | 4.40 ms: 1.11x faster                                                                                                      |
| xml_etree_generate         | 58.2 ms                                                                                                                | 52.5 ms: 1.11x faster                                                                                                      |
| json_dumps                 | 7.08 ms                                                                                                                | 6.45 ms: 1.10x faster                                                                                                      |
| pickle_pure_python         | 227 us                                                                                                                 | 207 us: 1.10x faster                                                                                                       |
| chaos                      | 44.3 ms                                                                                                                | 40.4 ms: 1.10x faster                                                                                                      |
| json                       | 3.21 ms                                                                                                                | 2.98 ms: 1.08x faster                                                                                                      |
| regex_compile              | 91.5 ms                                                                                                                | 85.2 ms: 1.07x faster                                                                                                      |
| meteor_contest             | 77.5 ms                                                                                                                | 72.2 ms: 1.07x faster                                                                                                      |
| dulwich_log                | 43.0 ms                                                                                                                | 40.2 ms: 1.07x faster                                                                                                      |
| html5lib                   | 40.9 ms                                                                                                                | 38.7 ms: 1.06x faster                                                                                                      |
| sqlglot_parse              | 919 us                                                                                                                 | 871 us: 1.05x faster                                                                                                       |
| connected_components       | 330 ms                                                                                                                 | 314 ms: 1.05x faster                                                                                                       |
| k_core                     | 2.11 sec                                                                                                               | 2.02 sec: 1.05x faster                                                                                                     |
| logging_simple             | 6.38 us                                                                                                                | 6.14 us: 1.04x faster                                                                                                      |
| deepcopy_reduce            | 1.93 us                                                                                                                | 1.85 us: 1.04x faster                                                                                                      |
| regex_v8                   | 15.4 ms                                                                                                                | 14.8 ms: 1.04x faster                                                                                                      |
| comprehensions             | 12.2 us                                                                                                                | 11.7 us: 1.04x faster                                                                                                      |
| pycparser                  | 741 ms                                                                                                                 | 715 ms: 1.04x faster                                                                                                       |
| xml_etree_iterparse        | 65.5 ms                                                                                                                | 63.6 ms: 1.03x faster                                                                                                      |
| shortest_path              | 358 ms                                                                                                                 | 349 ms: 1.03x faster                                                                                                       |
| sqlite_synth               | 1.61 us                                                                                                                | 1.58 us: 1.02x faster                                                                                                      |
| regex_effbot               | 1.44 ms                                                                                                                | 1.41 ms: 1.02x faster                                                                                                      |
| regex_dna                  | 116 ms                                                                                                                 | 113 ms: 1.02x faster                                                                                                       |
| typing_runtime_protocols   | 114 us                                                                                                                 | 113 us: 1.02x faster                                                                                                       |
| logging_format             | 6.72 us                                                                                                                | 6.61 us: 1.02x faster                                                                                                      |
| subparsers                 | 16.2 ms                                                                                                                | 16.0 ms: 1.01x faster                                                                                                      |
| async_tree_memoization     | 276 ms                                                                                                                 | 273 ms: 1.01x faster                                                                                                       |
| sqlglot_transpile          | 1.13 ms                                                                                                                | 1.12 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed_tg | 419 ms                                                                                                                 | 414 ms: 1.01x faster                                                                                                       |
| richards                   | 32.8 ms                                                                                                                | 32.4 ms: 1.01x faster                                                                                                      |
| gc_traversal               | 1.87 ms                                                                                                                | 1.86 ms: 1.01x faster                                                                                                      |
| pathlib                    | 74.5 ms                                                                                                                | 74.1 ms: 1.01x faster                                                                                                      |
| bench_mp_pool              | 81.7 ms                                                                                                                | 82.1 ms: 1.01x slower                                                                                                      |
| generators                 | 22.5 ms                                                                                                                | 22.6 ms: 1.01x slower                                                                                                      |
| deepcopy                   | 188 us                                                                                                                 | 189 us: 1.01x slower                                                                                                       |
| deltablue                  | 2.31 ms                                                                                                                | 2.33 ms: 1.01x slower                                                                                                      |
| richards_super             | 36.5 ms                                                                                                                | 36.8 ms: 1.01x slower                                                                                                      |
| thrift                     | 540 us                                                                                                                 | 546 us: 1.01x slower                                                                                                       |
| sympy_expand               | 308 ms                                                                                                                 | 312 ms: 1.01x slower                                                                                                       |
| sympy_str                  | 179 ms                                                                                                                 | 182 ms: 1.02x slower                                                                                                       |
| bench_thread_pool          | 809 us                                                                                                                 | 824 us: 1.02x slower                                                                                                       |
| sympy_integrate            | 13.5 ms                                                                                                                | 13.9 ms: 1.03x slower                                                                                                      |
| sphinx                     | 673 ms                                                                                                                 | 694 ms: 1.03x slower                                                                                                       |
| mdp                        | 1.50 sec                                                                                                               | 1.55 sec: 1.04x slower                                                                                                     |
| asyncio_websockets         | 301 ms                                                                                                                 | 314 ms: 1.04x slower                                                                                                       |
| coverage                   | 45.6 ms                                                                                                                | 47.6 ms: 1.04x slower                                                                                                      |
| sqlglot_optimize           | 36.6 ms                                                                                                                | 38.3 ms: 1.05x slower                                                                                                      |
| django_template            | 25.3 ms                                                                                                                | 26.6 ms: 1.05x slower                                                                                                      |
| sqlglot_normalize          | 200 ms                                                                                                                 | 211 ms: 1.06x slower                                                                                                       |
| sympy_sum                  | 89.7 ms                                                                                                                | 94.7 ms: 1.06x slower                                                                                                      |
| raytrace                   | 194 ms                                                                                                                 | 205 ms: 1.06x slower                                                                                                       |
| docutils                   | 1.69 sec                                                                                                               | 1.80 sec: 1.06x slower                                                                                                     |
| many_optionals             | 448 us                                                                                                                 | 479 us: 1.07x slower                                                                                                       |
| async_generators           | 248 ms                                                                                                                 | 266 ms: 1.07x slower                                                                                                       |
| pylint                     | 190 ms                                                                                                                 | 207 ms: 1.09x slower                                                                                                       |
| hexiom                     | 4.58 ms                                                                                                                | 5.03 ms: 1.10x slower                                                                                                      |
| genshi_text                | 16.9 ms                                                                                                                | 18.7 ms: 1.11x slower                                                                                                      |
| genshi_xml                 | 35.8 ms                                                                                                                | 43.9 ms: 1.22x slower                                                                                                      |
| Geometric mean             | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (16): async_tree_none, async_tree_io_tg, async_tree_none_tg, coroutines, pidigits, create_gc_cycles, go, python_startup_no_site, json_loads, nqueens, async_tree_io, 2to3, python_startup, xml_etree_parse, async_tree_memoization_tg, async_tree_cpu_io_mixed

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown