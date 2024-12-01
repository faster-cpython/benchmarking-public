# Results vs. base

- fork: python
- ref: 328187cc4fcdd578db42
- machine: linux-x86_64
- commit hash: 328187c
- commit date: 2024-11-30
- overall geometric mean: 1.013x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 286 ms                                                                                                                  | 297 ms: 1.04x slower                                                                                                        |
| docutils       | 2.91 sec                                                                                                                | 3.11 sec: 1.07x slower                                                                                                      |
| html5lib       | 71.8 ms                                                                                                                 | 71.1 ms: 1.01x faster                                                                                                       |
| sphinx         | 1.13 sec                                                                                                                | 1.19 sec: 1.05x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                                   | 1.04x slower                                                                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|--------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets | 390 ms                                                                                                                  | 387 ms: 1.01x faster                                                                                                        |
| coroutines         | 20.8 ms                                                                                                                 | 21.2 ms: 1.02x slower                                                                                                       |
| async_generators   | 452 ms                                                                                                                  | 473 ms: 1.05x slower                                                                                                        |
| Geometric mean     | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| float          | 82.9 ms                                                                                                                 | 81.9 ms: 1.01x faster                                                                                                       |
| nbody          | 88.5 ms                                                                                                                 | 87.7 ms: 1.01x faster                                                                                                       |
| pidigits       | 252 ms                                                                                                                  | 251 ms: 1.00x faster                                                                                                        |
| Geometric mean | (ref)                                                                                                                   | 1.01x faster                                                                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.18 ms                                                                                                                 | 3.20 ms: 1.01x slower                                                                                                       |
| regex_compile  | 139 ms                                                                                                                  | 141 ms: 1.02x slower                                                                                                        |
| regex_v8       | 24.5 ms                                                                                                                 | 25.5 ms: 1.04x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                   | 1.02x slower                                                                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 2.52 sec                                                                                                                | 2.16 sec: 1.17x faster                                                                                                      |
| unpickle_pure_python | 218 us                                                                                                                  | 201 us: 1.08x faster                                                                                                        |
| xml_etree_process    | 60.7 ms                                                                                                                 | 57.7 ms: 1.05x faster                                                                                                       |
| xml_etree_generate   | 85.0 ms                                                                                                                 | 82.2 ms: 1.03x faster                                                                                                       |
| xml_etree_iterparse  | 104 ms                                                                                                                  | 102 ms: 1.03x faster                                                                                                        |
| xml_etree_parse      | 146 ms                                                                                                                  | 145 ms: 1.01x faster                                                                                                        |
| json_dumps           | 11.5 ms                                                                                                                 | 11.4 ms: 1.01x faster                                                                                                       |
| Geometric mean       | (ref)                                                                                                                   | 1.04x faster                                                                                                                |

Benchmark hidden because not significant (2): json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| mako            | 10.8 ms                                                                                                                 | 9.45 ms: 1.14x faster                                                                                                       |
| django_template | 37.8 ms                                                                                                                 | 39.9 ms: 1.05x slower                                                                                                       |
| genshi_xml      | 55.8 ms                                                                                                                 | 62.6 ms: 1.12x slower                                                                                                       |
| genshi_text     | 25.2 ms                                                                                                                 | 28.5 ms: 1.13x slower                                                                                                       |
| Geometric mean  | (ref)                                                                                                                   | 1.04x slower                                                                                                                |

All benchmarks:
===============

| Benchmark                | results/bm-20241130-3.14.0a2+-328187c/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json | results/bm-20241130-3.14.0a2+-328187c-JIT/bm-20241130-pythonperf2-x86_64-python-328187cc4fcdd578db42-3.14.0a2+-328187c.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------------:|
| richards_super           | 58.2 ms                                                                                                                 | 48.3 ms: 1.20x faster                                                                                                       |
| tomli_loads              | 2.52 sec                                                                                                                | 2.16 sec: 1.17x faster                                                                                                      |
| richards                 | 51.8 ms                                                                                                                 | 44.2 ms: 1.17x faster                                                                                                       |
| mako                     | 10.8 ms                                                                                                                 | 9.45 ms: 1.14x faster                                                                                                       |
| scimark_sor              | 119 ms                                                                                                                  | 106 ms: 1.13x faster                                                                                                        |
| deltablue                | 3.54 ms                                                                                                                 | 3.24 ms: 1.09x faster                                                                                                       |
| logging_silent           | 103 ns                                                                                                                  | 94.8 ns: 1.08x faster                                                                                                       |
| unpickle_pure_python     | 218 us                                                                                                                  | 201 us: 1.08x faster                                                                                                        |
| connected_components     | 436 ms                                                                                                                  | 404 ms: 1.08x faster                                                                                                        |
| spectral_norm            | 100 ms                                                                                                                  | 93.6 ms: 1.07x faster                                                                                                       |
| telco                    | 8.12 ms                                                                                                                 | 7.65 ms: 1.06x faster                                                                                                       |
| xml_etree_process        | 60.7 ms                                                                                                                 | 57.7 ms: 1.05x faster                                                                                                       |
| shortest_path            | 458 ms                                                                                                                  | 438 ms: 1.05x faster                                                                                                        |
| dulwich_log              | 68.5 ms                                                                                                                 | 65.8 ms: 1.04x faster                                                                                                       |
| pyflate                  | 499 ms                                                                                                                  | 480 ms: 1.04x faster                                                                                                        |
| xml_etree_generate       | 85.0 ms                                                                                                                 | 82.2 ms: 1.03x faster                                                                                                       |
| xml_etree_iterparse      | 104 ms                                                                                                                  | 102 ms: 1.03x faster                                                                                                        |
| scimark_fft              | 315 ms                                                                                                                  | 308 ms: 1.02x faster                                                                                                        |
| create_gc_cycles         | 2.95 ms                                                                                                                 | 2.89 ms: 1.02x faster                                                                                                       |
| scimark_lu               | 96.9 ms                                                                                                                 | 95.3 ms: 1.02x faster                                                                                                       |
| float                    | 82.9 ms                                                                                                                 | 81.9 ms: 1.01x faster                                                                                                       |
| html5lib                 | 71.8 ms                                                                                                                 | 71.1 ms: 1.01x faster                                                                                                       |
| nbody                    | 88.5 ms                                                                                                                 | 87.7 ms: 1.01x faster                                                                                                       |
| asyncio_websockets       | 390 ms                                                                                                                  | 387 ms: 1.01x faster                                                                                                        |
| xml_etree_parse          | 146 ms                                                                                                                  | 145 ms: 1.01x faster                                                                                                        |
| json_dumps               | 11.5 ms                                                                                                                 | 11.4 ms: 1.01x faster                                                                                                       |
| sqlite_synth             | 2.83 us                                                                                                                 | 2.82 us: 1.00x faster                                                                                                       |
| pidigits                 | 252 ms                                                                                                                  | 251 ms: 1.00x faster                                                                                                        |
| regex_effbot             | 3.18 ms                                                                                                                 | 3.20 ms: 1.01x slower                                                                                                       |
| scimark_sparse_mat_mult  | 4.79 ms                                                                                                                 | 4.83 ms: 1.01x slower                                                                                                       |
| gc_traversal             | 6.20 ms                                                                                                                 | 6.26 ms: 1.01x slower                                                                                                       |
| subparsers               | 23.5 ms                                                                                                                 | 23.8 ms: 1.01x slower                                                                                                       |
| sqlalchemy_imperative    | 18.3 ms                                                                                                                 | 18.5 ms: 1.01x slower                                                                                                       |
| regex_compile            | 139 ms                                                                                                                  | 141 ms: 1.02x slower                                                                                                        |
| json                     | 5.20 ms                                                                                                                 | 5.28 ms: 1.02x slower                                                                                                       |
| crypto_pyaes             | 72.4 ms                                                                                                                 | 73.5 ms: 1.02x slower                                                                                                       |
| coroutines               | 20.8 ms                                                                                                                 | 21.2 ms: 1.02x slower                                                                                                       |
| bpe_tokeniser            | 4.86 sec                                                                                                                | 4.94 sec: 1.02x slower                                                                                                      |
| pycparser                | 1.25 sec                                                                                                                | 1.28 sec: 1.03x slower                                                                                                      |
| mdp                      | 2.54 sec                                                                                                                | 2.61 sec: 1.03x slower                                                                                                      |
| scimark_monte_carlo      | 66.2 ms                                                                                                                 | 68.0 ms: 1.03x slower                                                                                                       |
| pathlib                  | 16.0 ms                                                                                                                 | 16.5 ms: 1.03x slower                                                                                                       |
| pprint_safe_repr         | 796 ms                                                                                                                  | 820 ms: 1.03x slower                                                                                                        |
| pprint_pformat           | 1.62 sec                                                                                                                | 1.67 sec: 1.03x slower                                                                                                      |
| thrift                   | 859 us                                                                                                                  | 890 us: 1.04x slower                                                                                                        |
| many_optionals           | 1.03 ms                                                                                                                 | 1.07 ms: 1.04x slower                                                                                                       |
| 2to3                     | 286 ms                                                                                                                  | 297 ms: 1.04x slower                                                                                                        |
| sqlalchemy_declarative   | 141 ms                                                                                                                  | 147 ms: 1.04x slower                                                                                                        |
| deepcopy_reduce          | 2.92 us                                                                                                                 | 3.04 us: 1.04x slower                                                                                                       |
| regex_v8                 | 24.5 ms                                                                                                                 | 25.5 ms: 1.04x slower                                                                                                       |
| meteor_contest           | 126 ms                                                                                                                  | 132 ms: 1.04x slower                                                                                                        |
| sympy_integrate          | 23.7 ms                                                                                                                 | 24.7 ms: 1.04x slower                                                                                                       |
| async_generators         | 452 ms                                                                                                                  | 473 ms: 1.05x slower                                                                                                        |
| sphinx                   | 1.13 sec                                                                                                                | 1.19 sec: 1.05x slower                                                                                                      |
| django_template          | 37.8 ms                                                                                                                 | 39.9 ms: 1.05x slower                                                                                                       |
| bench_thread_pool        | 930 us                                                                                                                  | 981 us: 1.06x slower                                                                                                        |
| sympy_str                | 295 ms                                                                                                                  | 311 ms: 1.06x slower                                                                                                        |
| sqlglot_transpile        | 1.80 ms                                                                                                                 | 1.91 ms: 1.06x slower                                                                                                       |
| sympy_expand             | 502 ms                                                                                                                  | 531 ms: 1.06x slower                                                                                                        |
| typing_runtime_protocols | 173 us                                                                                                                  | 183 us: 1.06x slower                                                                                                        |
| sympy_sum                | 154 ms                                                                                                                  | 163 ms: 1.06x slower                                                                                                        |
| deepcopy                 | 294 us                                                                                                                  | 312 us: 1.06x slower                                                                                                        |
| sqlglot_parse            | 1.42 ms                                                                                                                 | 1.50 ms: 1.06x slower                                                                                                       |
| docutils                 | 2.91 sec                                                                                                                | 3.11 sec: 1.07x slower                                                                                                      |
| fannkuch                 | 362 ms                                                                                                                  | 389 ms: 1.07x slower                                                                                                        |
| sqlglot_optimize         | 59.9 ms                                                                                                                 | 64.2 ms: 1.07x slower                                                                                                       |
| chaos                    | 62.2 ms                                                                                                                 | 66.8 ms: 1.07x slower                                                                                                       |
| nqueens                  | 91.7 ms                                                                                                                 | 99.8 ms: 1.09x slower                                                                                                       |
| pylint                   | 307 ms                                                                                                                  | 334 ms: 1.09x slower                                                                                                        |
| sqlglot_normalize        | 120 ms                                                                                                                  | 132 ms: 1.10x slower                                                                                                        |
| genshi_xml               | 55.8 ms                                                                                                                 | 62.6 ms: 1.12x slower                                                                                                       |
| comprehensions           | 17.7 us                                                                                                                 | 19.8 us: 1.12x slower                                                                                                       |
| genshi_text              | 25.2 ms                                                                                                                 | 28.5 ms: 1.13x slower                                                                                                       |
| hexiom                   | 6.28 ms                                                                                                                 | 7.18 ms: 1.14x slower                                                                                                       |
| raytrace                 | 282 ms                                                                                                                  | 326 ms: 1.16x slower                                                                                                        |
| go                       | 136 ms                                                                                                                  | 158 ms: 1.16x slower                                                                                                        |
| generators               | 29.3 ms                                                                                                                 | 39.0 ms: 1.33x slower                                                                                                       |
| Geometric mean           | (ref)                                                                                                                   | 1.01x slower                                                                                                                |

Benchmark hidden because not significant (20): bench_mp_pool, k_core, logging_simple, deepcopy_memo, json_loads, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, python_startup_no_site, python_startup, djangocms, async_tree_none_tg, pickle_pure_python, coverage, logging_format, async_tree_io_tg, regex_dna, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x