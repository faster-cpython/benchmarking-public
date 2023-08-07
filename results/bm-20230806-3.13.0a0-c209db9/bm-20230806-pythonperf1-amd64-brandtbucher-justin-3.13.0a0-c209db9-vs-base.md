
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.72 sec                                                                   | 1.76 sec: 1.03x slower                                             |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 82.5 ms                                                                    | 79.8 ms: 1.03x faster                                              |
| float          | 58.5 ms                                                                    | 57.6 ms: 1.02x faster                                              |
| pidigits       | 147 ms                                                                     | 151 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 123 ms                                                                     | 124 ms: 1.01x slower                                               |
| regex_compile  | 95.6 ms                                                                    | 98.0 ms: 1.03x slower                                              |
| regex_effbot   | 1.64 ms                                                                    | 1.68 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict          | 20.5 us                                                                    | 18.6 us: 1.10x faster                                              |
| pickle               | 7.32 us                                                                    | 7.05 us: 1.04x faster                                              |
| xml_etree_parse      | 93.8 ms                                                                    | 92.7 ms: 1.01x faster                                              |
| tomli_loads          | 1.66 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| json_dumps           | 5.90 ms                                                                    | 5.86 ms: 1.01x faster                                              |
| xml_etree_generate   | 59.1 ms                                                                    | 58.8 ms: 1.01x faster                                              |
| json_loads           | 13.8 us                                                                    | 13.9 us: 1.01x slower                                              |
| xml_etree_iterparse  | 67.3 ms                                                                    | 68.0 ms: 1.01x slower                                              |
| pickle_pure_python   | 202 us                                                                     | 204 us: 1.01x slower                                               |
| pickle_list          | 2.84 us                                                                    | 2.88 us: 1.01x slower                                              |
| unpickle             | 8.34 us                                                                    | 8.61 us: 1.03x slower                                              |
| unpickle_pure_python | 148 us                                                                     | 154 us: 1.04x slower                                               |
| unpickle_list        | 2.88 us                                                                    | 3.04 us: 1.06x slower                                              |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup | 19.6 ms                                                                    | 19.4 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 7.94 ms                                                                    | 7.39 ms: 1.07x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_dict              | 20.5 us                                                                    | 18.6 us: 1.10x faster                                              |
| mako                     | 7.94 ms                                                                    | 7.39 ms: 1.07x faster                                              |
| pickle                   | 7.32 us                                                                    | 7.05 us: 1.04x faster                                              |
| nbody                    | 82.5 ms                                                                    | 79.8 ms: 1.03x faster                                              |
| coroutines               | 15.9 ms                                                                    | 15.5 ms: 1.03x faster                                              |
| logging_silent           | 68.9 ns                                                                    | 67.8 ns: 1.02x faster                                              |
| float                    | 58.5 ms                                                                    | 57.6 ms: 1.02x faster                                              |
| xml_etree_parse          | 93.8 ms                                                                    | 92.7 ms: 1.01x faster                                              |
| python_startup           | 19.6 ms                                                                    | 19.4 ms: 1.01x faster                                              |
| tomli_loads              | 1.66 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| pathlib                  | 85.1 ms                                                                    | 84.4 ms: 1.01x faster                                              |
| json_dumps               | 5.90 ms                                                                    | 5.86 ms: 1.01x faster                                              |
| gc_traversal             | 1.54 ms                                                                    | 1.53 ms: 1.01x faster                                              |
| xml_etree_generate       | 59.1 ms                                                                    | 58.8 ms: 1.01x faster                                              |
| typing_runtime_protocols | 98.5 us                                                                    | 98.0 us: 1.01x faster                                              |
| dulwich_log              | 47.7 ms                                                                    | 48.1 ms: 1.01x slower                                              |
| mdp                      | 1.56 sec                                                                   | 1.57 sec: 1.01x slower                                             |
| regex_dna                | 123 ms                                                                     | 124 ms: 1.01x slower                                               |
| deepcopy_reduce          | 2.29 us                                                                    | 2.31 us: 1.01x slower                                              |
| json_loads               | 13.8 us                                                                    | 13.9 us: 1.01x slower                                              |
| generators               | 26.8 ms                                                                    | 27.0 ms: 1.01x slower                                              |
| xml_etree_iterparse      | 67.3 ms                                                                    | 68.0 ms: 1.01x slower                                              |
| logging_simple           | 6.93 us                                                                    | 7.01 us: 1.01x slower                                              |
| pickle_pure_python       | 202 us                                                                     | 204 us: 1.01x slower                                               |
| pickle_list              | 2.84 us                                                                    | 2.88 us: 1.01x slower                                              |
| sqlglot_transpile        | 1.14 ms                                                                    | 1.15 ms: 1.01x slower                                              |
| dask                     | 393 ms                                                                     | 398 ms: 1.01x slower                                               |
| crypto_pyaes             | 47.7 ms                                                                    | 48.4 ms: 1.01x slower                                              |
| nqueens                  | 66.0 ms                                                                    | 66.9 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed  | 502 ms                                                                     | 510 ms: 1.02x slower                                               |
| telco                    | 4.80 ms                                                                    | 4.88 ms: 1.02x slower                                              |
| async_tree_none          | 313 ms                                                                     | 319 ms: 1.02x slower                                               |
| sqlglot_normalize        | 198 ms                                                                     | 201 ms: 1.02x slower                                               |
| sqlglot_optimize         | 36.5 ms                                                                    | 37.2 ms: 1.02x slower                                              |
| deepcopy                 | 256 us                                                                     | 261 us: 1.02x slower                                               |
| scimark_lu               | 64.0 ms                                                                    | 65.4 ms: 1.02x slower                                              |
| deepcopy_memo            | 26.2 us                                                                    | 26.8 us: 1.02x slower                                              |
| pidigits                 | 147 ms                                                                     | 151 ms: 1.02x slower                                               |
| regex_compile            | 95.6 ms                                                                    | 98.0 ms: 1.03x slower                                              |
| bench_thread_pool        | 842 us                                                                     | 864 us: 1.03x slower                                               |
| richards                 | 30.8 ms                                                                    | 31.6 ms: 1.03x slower                                              |
| sqlite_synth             | 1.77 us                                                                    | 1.81 us: 1.03x slower                                              |
| pprint_pformat           | 1.11 sec                                                                   | 1.14 sec: 1.03x slower                                             |
| docutils                 | 1.72 sec                                                                   | 1.76 sec: 1.03x slower                                             |
| scimark_monte_carlo      | 45.0 ms                                                                    | 46.2 ms: 1.03x slower                                              |
| raytrace                 | 190 ms                                                                     | 195 ms: 1.03x slower                                               |
| regex_effbot             | 1.64 ms                                                                    | 1.68 ms: 1.03x slower                                              |
| pyflate                  | 324 ms                                                                     | 334 ms: 1.03x slower                                               |
| unpickle                 | 8.34 us                                                                    | 8.61 us: 1.03x slower                                              |
| pprint_safe_repr         | 543 ms                                                                     | 561 ms: 1.03x slower                                               |
| unpickle_pure_python     | 148 us                                                                     | 154 us: 1.04x slower                                               |
| mypy2                    | 222 ms                                                                     | 232 ms: 1.04x slower                                               |
| bench_mp_pool            | 67.9 ms                                                                    | 71.1 ms: 1.05x slower                                              |
| go                       | 102 ms                                                                     | 107 ms: 1.05x slower                                               |
| json                     | 2.87 ms                                                                    | 3.03 ms: 1.06x slower                                              |
| scimark_fft              | 190 ms                                                                     | 201 ms: 1.06x slower                                               |
| spectral_norm            | 70.9 ms                                                                    | 74.9 ms: 1.06x slower                                              |
| unpickle_list            | 2.88 us                                                                    | 3.04 us: 1.06x slower                                              |
| comprehensions           | 15.6 us                                                                    | 16.6 us: 1.06x slower                                              |
| scimark_sor              | 86.3 ms                                                                    | 91.9 ms: 1.06x slower                                              |
| meteor_contest           | 76.9 ms                                                                    | 82.1 ms: 1.07x slower                                              |
| chaos                    | 44.6 ms                                                                    | 47.9 ms: 1.07x slower                                              |
| fannkuch                 | 261 ms                                                                     | 284 ms: 1.09x slower                                               |
| unpack_sequence          | 38.5 ns                                                                    | 42.0 ns: 1.09x slower                                              |
| hexiom                   | 4.64 ms                                                                    | 5.06 ms: 1.09x slower                                              |
| scimark_sparse_mat_mult  | 2.61 ms                                                                    | 3.01 ms: 1.15x slower                                              |
| Geometric mean           | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (16): regex_v8, pycparser, asyncio_tcp_ssl, create_gc_cycles, logging_format, async_tree_io, coverage, async_generators, python_startup_no_site, xml_etree_process, deltablue, sqlglot_parse, async_tree_memoization, richards_super, tornado_http, asyncio_tcp
