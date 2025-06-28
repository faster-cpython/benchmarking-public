# Results vs. 3.13.0

- fork: python
- ref: c419af9e277bea7dd78f
- machine: windows-amd64
- commit hash: c419af9
- commit date: 2025-06-28
- overall geometric mean: 1.077x faster
- HPT reliability: 78.53%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 647 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.5 ms: 1.24x faster                                                      |
| float          | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.70x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 108 us: 1.20x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| xml_etree_generate   | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 34.6 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.54 ms: 1.19x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 500 us: 16.94x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.39x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                       |
| mdp                        | 1.43 sec                                                    | 806 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.70x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 171 ms: 1.28x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.1 us: 1.28x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| nbody                      | 66.3 ms                                                     | 53.5 ms: 1.24x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 108 us: 1.20x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.19x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.54 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| scimark_fft                | 175 ms                                                      | 152 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.25 ms: 1.14x faster                                                      |
| float                      | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.54 sec: 1.13x faster                                                     |
| fannkuch                   | 252 ms                                                      | 224 ms: 1.12x faster                                                       |
| json                       | 3.30 ms                                                     | 2.94 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                      |
| pyflate                    | 283 ms                                                      | 257 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 453 ms: 1.07x faster                                                       |
| go                         | 84.7 ms                                                     | 79.3 ms: 1.07x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 915 ms: 1.07x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 34.6 ms: 1.05x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.03x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.03x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 90.4 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.2 ms: 1.01x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.2 ms: 1.01x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.5 ms: 1.02x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.02x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.3 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 647 ms: 1.05x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.2 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| shortest_path              | 355 ms                                                      | 374 ms: 1.05x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.05x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.56 us: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.1 ms: 1.07x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.19 us: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                      | 242 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| chaos                      | 37.9 ms                                                     | 41.2 ms: 1.09x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 83.0 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.4 ms: 1.10x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.25 ms: 1.11x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.0 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 15.0 ms: 1.20x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.27 ms: 1.20x slower                                                      |
| raytrace                   | 153 ms                                                      | 186 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (5): pylint, pidigits, logging_silent, pycparser, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250628-3.15.0a0-c419af9-JIT/bm-20250628-pythonperf1-amd64-python-c419af9e277bea7dd78f-3.15.0a0-c419af9.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.077x faster

# HPT report

- Reliability score: 78.53% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown