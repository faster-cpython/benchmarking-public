# Results vs. base

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.053x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 227 ms                                                                                                                 | 221 ms: 1.03x faster                                                                                                       |
| docutils       | 1.68 sec                                                                                                               | 1.73 sec: 1.03x slower                                                                                                     |
| sphinx         | 655 ms                                                                                                                 | 688 ms: 1.05x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.01x slower                                                                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg        | 173 ms                                                                                                                 | 170 ms: 1.02x faster                                                                                                       |
| async_tree_io_tg          | 403 ms                                                                                                                 | 398 ms: 1.01x faster                                                                                                       |
| asyncio_websockets        | 308 ms                                                                                                                 | 304 ms: 1.01x faster                                                                                                       |
| async_tree_io             | 410 ms                                                                                                                 | 406 ms: 1.01x faster                                                                                                       |
| coroutines                | 13.7 ms                                                                                                                | 13.5 ms: 1.01x faster                                                                                                      |
| async_tree_cpu_io_mixed   | 348 ms                                                                                                                 | 353 ms: 1.02x slower                                                                                                       |
| async_tree_memoization_tg | 211 ms                                                                                                                 | 214 ms: 1.02x slower                                                                                                       |
| async_generators          | 238 ms                                                                                                                 | 251 ms: 1.05x slower                                                                                                       |
| Geometric mean            | (ref)                                                                                                                  | 1.00x slower                                                                                                               |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody          | 83.2 ms                                                                                                                | 54.3 ms: 1.53x faster                                                                                                      |
| float          | 55.4 ms                                                                                                                | 47.3 ms: 1.17x faster                                                                                                      |
| pidigits       | 147 ms                                                                                                                 | 147 ms: 1.00x slower                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.21x faster                                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 21.5 ms                                                                                                                | 18.4 ms: 1.17x faster                                                                                                      |
| regex_compile  | 88.2 ms                                                                                                                | 80.0 ms: 1.10x faster                                                                                                      |
| regex_effbot   | 1.53 ms                                                                                                                | 1.44 ms: 1.06x faster                                                                                                      |
| regex_dna      | 119 ms                                                                                                                 | 115 ms: 1.04x faster                                                                                                       |
| Geometric mean | (ref)                                                                                                                  | 1.09x faster                                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|----------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                                                                                 | 110 us: 1.38x faster                                                                                                       |
| tomli_loads          | 1.43 sec                                                                                                               | 1.18 sec: 1.21x faster                                                                                                     |
| xml_etree_generate   | 57.7 ms                                                                                                                | 50.3 ms: 1.15x faster                                                                                                      |
| xml_etree_process    | 40.8 ms                                                                                                                | 35.9 ms: 1.14x faster                                                                                                      |
| pickle_pure_python   | 227 us                                                                                                                 | 205 us: 1.11x faster                                                                                                       |
| xml_etree_iterparse  | 63.1 ms                                                                                                                | 58.8 ms: 1.07x faster                                                                                                      |
| json_dumps           | 6.66 ms                                                                                                                | 6.29 ms: 1.06x faster                                                                                                      |
| Geometric mean       | (ref)                                                                                                                  | 1.12x faster                                                                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                                                                                | 17.4 ms: 1.04x faster                                                                                                      |
| python_startup         | 24.2 ms                                                                                                                | 23.4 ms: 1.04x faster                                                                                                      |
| Geometric mean         | (ref)                                                                                                                  | 1.04x faster                                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|-----------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.03 ms                                                                                                                | 5.11 ms: 1.38x faster                                                                                                      |
| django_template | 25.1 ms                                                                                                                | 26.8 ms: 1.07x slower                                                                                                      |
| genshi_text     | 16.8 ms                                                                                                                | 18.3 ms: 1.09x slower                                                                                                      |
| genshi_xml      | 35.1 ms                                                                                                                | 47.5 ms: 1.35x slower                                                                                                      |
| Geometric mean  | (ref)                                                                                                                  | 1.03x slower                                                                                                               |

All benchmarks:
===============

| Benchmark                 | results/bm-20241228-3.14.0a3+-f9a5a3a/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json | results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json |
|---------------------------|:----------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------:|
| nbody                     | 83.2 ms                                                                                                                | 54.3 ms: 1.53x faster                                                                                                      |
| scimark_sor               | 88.8 ms                                                                                                                | 61.5 ms: 1.44x faster                                                                                                      |
| unpickle_pure_python      | 151 us                                                                                                                 | 110 us: 1.38x faster                                                                                                       |
| mako                      | 7.03 ms                                                                                                                | 5.11 ms: 1.38x faster                                                                                                      |
| scimark_fft               | 193 ms                                                                                                                 | 147 ms: 1.31x faster                                                                                                       |
| scimark_monte_carlo       | 47.7 ms                                                                                                                | 36.7 ms: 1.30x faster                                                                                                      |
| spectral_norm             | 62.8 ms                                                                                                                | 48.6 ms: 1.29x faster                                                                                                      |
| deepcopy_memo             | 21.3 us                                                                                                                | 16.9 us: 1.26x faster                                                                                                      |
| scimark_sparse_mat_mult   | 2.66 ms                                                                                                                | 2.12 ms: 1.25x faster                                                                                                      |
| tomli_loads               | 1.43 sec                                                                                                               | 1.18 sec: 1.21x faster                                                                                                     |
| crypto_pyaes              | 49.5 ms                                                                                                                | 41.1 ms: 1.20x faster                                                                                                      |
| fannkuch                  | 287 ms                                                                                                                 | 243 ms: 1.18x faster                                                                                                       |
| regex_v8                  | 21.5 ms                                                                                                                | 18.4 ms: 1.17x faster                                                                                                      |
| float                     | 55.4 ms                                                                                                                | 47.3 ms: 1.17x faster                                                                                                      |
| scimark_lu                | 63.3 ms                                                                                                                | 54.5 ms: 1.16x faster                                                                                                      |
| bpe_tokeniser             | 3.04 sec                                                                                                               | 2.62 sec: 1.16x faster                                                                                                     |
| xml_etree_generate        | 57.7 ms                                                                                                                | 50.3 ms: 1.15x faster                                                                                                      |
| logging_silent            | 65.8 ns                                                                                                                | 57.5 ns: 1.14x faster                                                                                                      |
| telco                     | 4.89 ms                                                                                                                | 4.30 ms: 1.14x faster                                                                                                      |
| xml_etree_process         | 40.8 ms                                                                                                                | 35.9 ms: 1.14x faster                                                                                                      |
| pprint_pformat            | 1.12 sec                                                                                                               | 985 ms: 1.14x faster                                                                                                       |
| pyflate                   | 316 ms                                                                                                                 | 279 ms: 1.13x faster                                                                                                       |
| pprint_safe_repr          | 553 ms                                                                                                                 | 495 ms: 1.12x faster                                                                                                       |
| pickle_pure_python        | 227 us                                                                                                                 | 205 us: 1.11x faster                                                                                                       |
| regex_compile             | 88.2 ms                                                                                                                | 80.0 ms: 1.10x faster                                                                                                      |
| sqlglot_parse             | 909 us                                                                                                                 | 844 us: 1.08x faster                                                                                                       |
| xml_etree_iterparse       | 63.1 ms                                                                                                                | 58.8 ms: 1.07x faster                                                                                                      |
| k_core                    | 1.70 sec                                                                                                               | 1.59 sec: 1.07x faster                                                                                                     |
| bench_mp_pool             | 88.0 ms                                                                                                                | 82.6 ms: 1.07x faster                                                                                                      |
| regex_effbot              | 1.53 ms                                                                                                                | 1.44 ms: 1.06x faster                                                                                                      |
| json_dumps                | 6.66 ms                                                                                                                | 6.29 ms: 1.06x faster                                                                                                      |
| comprehensions            | 12.5 us                                                                                                                | 11.9 us: 1.06x faster                                                                                                      |
| dulwich_log               | 42.7 ms                                                                                                                | 40.5 ms: 1.05x faster                                                                                                      |
| chaos                     | 43.5 ms                                                                                                                | 41.4 ms: 1.05x faster                                                                                                      |
| nqueens                   | 66.3 ms                                                                                                                | 63.3 ms: 1.05x faster                                                                                                      |
| meteor_contest            | 77.8 ms                                                                                                                | 74.3 ms: 1.05x faster                                                                                                      |
| python_startup_no_site    | 18.1 ms                                                                                                                | 17.4 ms: 1.04x faster                                                                                                      |
| connected_components      | 321 ms                                                                                                                 | 309 ms: 1.04x faster                                                                                                       |
| regex_dna                 | 119 ms                                                                                                                 | 115 ms: 1.04x faster                                                                                                       |
| shortest_path             | 353 ms                                                                                                                 | 341 ms: 1.04x faster                                                                                                       |
| python_startup            | 24.2 ms                                                                                                                | 23.4 ms: 1.04x faster                                                                                                      |
| sqlglot_transpile         | 1.13 ms                                                                                                                | 1.09 ms: 1.03x faster                                                                                                      |
| deepcopy_reduce           | 1.90 us                                                                                                                | 1.85 us: 1.03x faster                                                                                                      |
| 2to3                      | 227 ms                                                                                                                 | 221 ms: 1.03x faster                                                                                                       |
| logging_simple            | 6.44 us                                                                                                                | 6.26 us: 1.03x faster                                                                                                      |
| go                        | 90.9 ms                                                                                                                | 88.8 ms: 1.02x faster                                                                                                      |
| deltablue                 | 2.30 ms                                                                                                                | 2.25 ms: 1.02x faster                                                                                                      |
| sqlite_synth              | 1.61 us                                                                                                                | 1.58 us: 1.02x faster                                                                                                      |
| async_tree_none_tg        | 173 ms                                                                                                                 | 170 ms: 1.02x faster                                                                                                       |
| logging_format            | 6.83 us                                                                                                                | 6.71 us: 1.02x faster                                                                                                      |
| async_tree_io_tg          | 403 ms                                                                                                                 | 398 ms: 1.01x faster                                                                                                       |
| asyncio_websockets        | 308 ms                                                                                                                 | 304 ms: 1.01x faster                                                                                                       |
| subparsers                | 16.3 ms                                                                                                                | 16.1 ms: 1.01x faster                                                                                                      |
| async_tree_io             | 410 ms                                                                                                                 | 406 ms: 1.01x faster                                                                                                       |
| coroutines                | 13.7 ms                                                                                                                | 13.5 ms: 1.01x faster                                                                                                      |
| coverage                  | 46.9 ms                                                                                                                | 46.6 ms: 1.01x faster                                                                                                      |
| pidigits                  | 147 ms                                                                                                                 | 147 ms: 1.00x slower                                                                                                       |
| sympy_sum                 | 90.4 ms                                                                                                                | 91.7 ms: 1.01x slower                                                                                                      |
| async_tree_cpu_io_mixed   | 348 ms                                                                                                                 | 353 ms: 1.02x slower                                                                                                       |
| create_gc_cycles          | 1.20 ms                                                                                                                | 1.22 ms: 1.02x slower                                                                                                      |
| async_tree_memoization_tg | 211 ms                                                                                                                 | 214 ms: 1.02x slower                                                                                                       |
| deepcopy                  | 186 us                                                                                                                 | 190 us: 1.02x slower                                                                                                       |
| docutils                  | 1.68 sec                                                                                                               | 1.73 sec: 1.03x slower                                                                                                     |
| mdp                       | 1.48 sec                                                                                                               | 1.52 sec: 1.03x slower                                                                                                     |
| thrift                    | 525 us                                                                                                                 | 544 us: 1.04x slower                                                                                                       |
| richards_super            | 36.2 ms                                                                                                                | 37.7 ms: 1.04x slower                                                                                                      |
| richards                  | 32.1 ms                                                                                                                | 33.6 ms: 1.04x slower                                                                                                      |
| pylint                    | 199 ms                                                                                                                 | 208 ms: 1.04x slower                                                                                                       |
| sqlglot_normalize         | 196 ms                                                                                                                 | 205 ms: 1.05x slower                                                                                                       |
| sphinx                    | 655 ms                                                                                                                 | 688 ms: 1.05x slower                                                                                                       |
| async_generators          | 238 ms                                                                                                                 | 251 ms: 1.05x slower                                                                                                       |
| sqlglot_optimize          | 35.8 ms                                                                                                                | 37.8 ms: 1.05x slower                                                                                                      |
| many_optionals            | 438 us                                                                                                                 | 467 us: 1.06x slower                                                                                                       |
| django_template           | 25.1 ms                                                                                                                | 26.8 ms: 1.07x slower                                                                                                      |
| raytrace                  | 198 ms                                                                                                                 | 213 ms: 1.08x slower                                                                                                       |
| genshi_text               | 16.8 ms                                                                                                                | 18.3 ms: 1.09x slower                                                                                                      |
| hexiom                    | 4.59 ms                                                                                                                | 5.01 ms: 1.09x slower                                                                                                      |
| generators                | 21.2 ms                                                                                                                | 24.2 ms: 1.14x slower                                                                                                      |
| genshi_xml                | 35.1 ms                                                                                                                | 47.5 ms: 1.35x slower                                                                                                      |
| Geometric mean            | (ref)                                                                                                                  | 1.05x faster                                                                                                               |

Benchmark hidden because not significant (16): json, pycparser, async_tree_memoization, xml_etree_parse, sympy_str, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_none, html5lib, typing_runtime_protocols, json_loads, sympy_expand, sympy_integrate, mypy2, pathlib, gc_traversal

- Geometric mean (including insignificant results): 1.053x faster

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown