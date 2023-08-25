
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: windows-amd64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 1.71 sec                                                                   | 1.76 sec: 1.03x slower                                             |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 82.2 ms                                                                    | 79.8 ms: 1.03x faster                                              |
| float          | 58.7 ms                                                                    | 57.6 ms: 1.02x faster                                              |
| pidigits       | 149 ms                                                                     | 151 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                      | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 122 ms                                                                     | 124 ms: 1.01x slower                                               |
| regex_compile  | 96.4 ms                                                                    | 98.0 ms: 1.02x slower                                              |
| regex_effbot   | 1.65 ms                                                                    | 1.68 ms: 1.02x slower                                              |
| regex_v8       | 13.6 ms                                                                    | 14.1 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle               | 7.39 us                                                                    | 7.05 us: 1.05x faster                                              |
| xml_etree_parse      | 95.5 ms                                                                    | 92.7 ms: 1.03x faster                                              |
| pickle_dict          | 19.1 us                                                                    | 18.6 us: 1.03x faster                                              |
| xml_etree_process    | 40.8 ms                                                                    | 40.4 ms: 1.01x faster                                              |
| tomli_loads          | 1.65 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| json_dumps           | 5.80 ms                                                                    | 5.86 ms: 1.01x slower                                              |
| pickle_list          | 2.84 us                                                                    | 2.88 us: 1.01x slower                                              |
| unpickle             | 8.45 us                                                                    | 8.61 us: 1.02x slower                                              |
| xml_etree_iterparse  | 66.3 ms                                                                    | 68.0 ms: 1.03x slower                                              |
| unpickle_pure_python | 150 us                                                                     | 154 us: 1.03x slower                                               |
| unpickle_list        | 2.81 us                                                                    | 3.04 us: 1.08x slower                                              |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                       |

Benchmark hidden because not significant (3): xml_etree_generate, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                                    | 16.7 ms: 1.03x slower                                              |
| Geometric mean         | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 8.01 ms                                                                    | 7.39 ms: 1.08x faster                                              |

All benchmarks:
===============

| Benchmark               | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-justin-3.13.0a0-c209db9 |
|-------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako                    | 8.01 ms                                                                    | 7.39 ms: 1.08x faster                                              |
| coroutines              | 16.5 ms                                                                    | 15.5 ms: 1.07x faster                                              |
| pickle                  | 7.39 us                                                                    | 7.05 us: 1.05x faster                                              |
| nbody                   | 82.2 ms                                                                    | 79.8 ms: 1.03x faster                                              |
| xml_etree_parse         | 95.5 ms                                                                    | 92.7 ms: 1.03x faster                                              |
| pickle_dict             | 19.1 us                                                                    | 18.6 us: 1.03x faster                                              |
| float                   | 58.7 ms                                                                    | 57.6 ms: 1.02x faster                                              |
| logging_silent          | 69.1 ns                                                                    | 67.8 ns: 1.02x faster                                              |
| generators              | 27.5 ms                                                                    | 27.0 ms: 1.02x faster                                              |
| logging_simple          | 7.12 us                                                                    | 7.01 us: 1.02x faster                                              |
| logging_format          | 7.65 us                                                                    | 7.54 us: 1.01x faster                                              |
| xml_etree_process       | 40.8 ms                                                                    | 40.4 ms: 1.01x faster                                              |
| tomli_loads             | 1.65 sec                                                                   | 1.64 sec: 1.01x faster                                             |
| deltablue               | 2.41 ms                                                                    | 2.42 ms: 1.01x slower                                              |
| sqlglot_normalize       | 200 ms                                                                     | 201 ms: 1.01x slower                                               |
| json_dumps              | 5.80 ms                                                                    | 5.86 ms: 1.01x slower                                              |
| coverage                | 52.2 ms                                                                    | 52.7 ms: 1.01x slower                                              |
| dask                    | 394 ms                                                                     | 398 ms: 1.01x slower                                               |
| pprint_pformat          | 1.13 sec                                                                   | 1.14 sec: 1.01x slower                                             |
| pidigits                | 149 ms                                                                     | 151 ms: 1.01x slower                                               |
| pickle_list             | 2.84 us                                                                    | 2.88 us: 1.01x slower                                              |
| async_generators        | 248 ms                                                                     | 252 ms: 1.01x slower                                               |
| regex_dna               | 122 ms                                                                     | 124 ms: 1.01x slower                                               |
| regex_compile           | 96.4 ms                                                                    | 98.0 ms: 1.02x slower                                              |
| async_tree_none         | 313 ms                                                                     | 319 ms: 1.02x slower                                               |
| richards                | 31.1 ms                                                                    | 31.6 ms: 1.02x slower                                              |
| unpickle                | 8.45 us                                                                    | 8.61 us: 1.02x slower                                              |
| pyflate                 | 327 ms                                                                     | 334 ms: 1.02x slower                                               |
| regex_effbot            | 1.65 ms                                                                    | 1.68 ms: 1.02x slower                                              |
| deepcopy_reduce         | 2.25 us                                                                    | 2.31 us: 1.02x slower                                              |
| dulwich_log             | 46.9 ms                                                                    | 48.1 ms: 1.02x slower                                              |
| crypto_pyaes            | 47.1 ms                                                                    | 48.4 ms: 1.03x slower                                              |
| xml_etree_iterparse     | 66.3 ms                                                                    | 68.0 ms: 1.03x slower                                              |
| mypy2                   | 226 ms                                                                     | 232 ms: 1.03x slower                                               |
| sqlite_synth            | 1.76 us                                                                    | 1.81 us: 1.03x slower                                              |
| unpickle_pure_python    | 150 us                                                                     | 154 us: 1.03x slower                                               |
| python_startup_no_site  | 16.2 ms                                                                    | 16.7 ms: 1.03x slower                                              |
| docutils                | 1.71 sec                                                                   | 1.76 sec: 1.03x slower                                             |
| pprint_safe_repr        | 544 ms                                                                     | 561 ms: 1.03x slower                                               |
| scimark_monte_carlo     | 44.8 ms                                                                    | 46.2 ms: 1.03x slower                                              |
| telco                   | 4.72 ms                                                                    | 4.88 ms: 1.03x slower                                              |
| nqueens                 | 64.6 ms                                                                    | 66.9 ms: 1.03x slower                                              |
| regex_v8                | 13.6 ms                                                                    | 14.1 ms: 1.04x slower                                              |
| deepcopy                | 252 us                                                                     | 261 us: 1.04x slower                                               |
| scimark_lu              | 63.0 ms                                                                    | 65.4 ms: 1.04x slower                                              |
| deepcopy_memo           | 25.7 us                                                                    | 26.8 us: 1.04x slower                                              |
| comprehensions          | 15.8 us                                                                    | 16.6 us: 1.05x slower                                              |
| bench_mp_pool           | 67.7 ms                                                                    | 71.1 ms: 1.05x slower                                              |
| scimark_sor             | 86.9 ms                                                                    | 91.9 ms: 1.06x slower                                              |
| scimark_fft             | 189 ms                                                                     | 201 ms: 1.06x slower                                               |
| go                      | 101 ms                                                                     | 107 ms: 1.06x slower                                               |
| json                    | 2.85 ms                                                                    | 3.03 ms: 1.06x slower                                              |
| chaos                   | 44.6 ms                                                                    | 47.9 ms: 1.07x slower                                              |
| mdp                     | 1.46 sec                                                                   | 1.57 sec: 1.07x slower                                             |
| unpickle_list           | 2.81 us                                                                    | 3.04 us: 1.08x slower                                              |
| fannkuch                | 262 ms                                                                     | 284 ms: 1.08x slower                                               |
| spectral_norm           | 68.8 ms                                                                    | 74.9 ms: 1.09x slower                                              |
| meteor_contest          | 75.4 ms                                                                    | 82.1 ms: 1.09x slower                                              |
| hexiom                  | 4.64 ms                                                                    | 5.06 ms: 1.09x slower                                              |
| unpack_sequence         | 38.4 ns                                                                    | 42.0 ns: 1.09x slower                                              |
| scimark_sparse_mat_mult | 2.60 ms                                                                    | 3.01 ms: 1.16x slower                                              |
| Geometric mean          | (ref)                                                                      | 1.02x slower                                                       |

Benchmark hidden because not significant (21): pycparser, async_tree_memoization, sqlglot_parse, tornado_http, xml_etree_generate, async_tree_cpu_io_mixed, pickle_pure_python, create_gc_cycles, sqlglot_optimize, richards_super, raytrace, sqlglot_transpile, bench_thread_pool, json_loads, typing_runtime_protocols, gc_traversal, async_tree_io, asyncio_tcp, pathlib, python_startup, asyncio_tcp_ssl


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
