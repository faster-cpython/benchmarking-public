
# Results vs. base

- fork: brandtbucher
- ref: uops_enabled
- machine: windows-amd64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.71 sec                                                                   | 1.76 sec: 1.03x slower                                                   |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 149 ms                                                                     | 148 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                             |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 1.65 ms                                                                    | 1.61 ms: 1.02x faster                                                    |
| regex_v8       | 13.6 ms                                                                    | 13.9 ms: 1.02x slower                                                    |
| regex_compile  | 96.4 ms                                                                    | 101 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_dict          | 19.1 us                                                                    | 18.5 us: 1.03x faster                                                    |
| unpickle             | 8.45 us                                                                    | 8.21 us: 1.03x faster                                                    |
| xml_etree_parse      | 95.5 ms                                                                    | 93.2 ms: 1.02x faster                                                    |
| json_loads           | 13.9 us                                                                    | 13.7 us: 1.02x faster                                                    |
| pickle_pure_python   | 204 us                                                                     | 202 us: 1.01x faster                                                     |
| pickle               | 7.39 us                                                                    | 7.45 us: 1.01x slower                                                    |
| json_dumps           | 5.80 ms                                                                    | 5.87 ms: 1.01x slower                                                    |
| pickle_list          | 2.84 us                                                                    | 2.87 us: 1.01x slower                                                    |
| xml_etree_generate   | 59.0 ms                                                                    | 59.9 ms: 1.02x slower                                                    |
| unpickle_pure_python | 150 us                                                                     | 154 us: 1.03x slower                                                     |
| xml_etree_iterparse  | 66.3 ms                                                                    | 68.4 ms: 1.03x slower                                                    |
| unpickle_list        | 2.81 us                                                                    | 2.93 us: 1.04x slower                                                    |
| tomli_loads          | 1.65 sec                                                                   | 1.77 sec: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 19.2 ms                                                                    | 19.0 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                      | 1.00x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako      | 8.01 ms                                                                    | 8.28 ms: 1.03x slower                                                    |

All benchmarks:
===============

| Benchmark                | bm-20230806-pythonperf1-amd64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf1-amd64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines               | 16.5 ms                                                                    | 15.4 ms: 1.07x faster                                                    |
| generators               | 27.5 ms                                                                    | 25.7 ms: 1.07x faster                                                    |
| pycparser                | 802 ms                                                                     | 772 ms: 1.04x faster                                                     |
| pickle_dict              | 19.1 us                                                                    | 18.5 us: 1.03x faster                                                    |
| unpickle                 | 8.45 us                                                                    | 8.21 us: 1.03x faster                                                    |
| xml_etree_parse          | 95.5 ms                                                                    | 93.2 ms: 1.02x faster                                                    |
| regex_effbot             | 1.65 ms                                                                    | 1.61 ms: 1.02x faster                                                    |
| logging_silent           | 69.1 ns                                                                    | 67.5 ns: 1.02x faster                                                    |
| async_tree_memoization   | 372 ms                                                                     | 364 ms: 1.02x faster                                                     |
| sqlglot_parse            | 918 us                                                                     | 903 us: 1.02x faster                                                     |
| json_loads               | 13.9 us                                                                    | 13.7 us: 1.02x faster                                                    |
| python_startup           | 19.2 ms                                                                    | 19.0 ms: 1.01x faster                                                    |
| pickle_pure_python       | 204 us                                                                     | 202 us: 1.01x faster                                                     |
| pidigits                 | 149 ms                                                                     | 148 ms: 1.01x faster                                                     |
| bench_mp_pool            | 67.7 ms                                                                    | 68.0 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 544 ms                                                                     | 548 ms: 1.01x slower                                                     |
| scimark_sor              | 86.9 ms                                                                    | 87.6 ms: 1.01x slower                                                    |
| pickle                   | 7.39 us                                                                    | 7.45 us: 1.01x slower                                                    |
| sqlite_synth             | 1.76 us                                                                    | 1.78 us: 1.01x slower                                                    |
| json_dumps               | 5.80 ms                                                                    | 5.87 ms: 1.01x slower                                                    |
| pickle_list              | 2.84 us                                                                    | 2.87 us: 1.01x slower                                                    |
| coverage                 | 52.2 ms                                                                    | 52.9 ms: 1.01x slower                                                    |
| pathlib                  | 83.9 ms                                                                    | 85.1 ms: 1.01x slower                                                    |
| deepcopy_reduce          | 2.25 us                                                                    | 2.28 us: 1.01x slower                                                    |
| gc_traversal             | 1.53 ms                                                                    | 1.55 ms: 1.01x slower                                                    |
| xml_etree_generate       | 59.0 ms                                                                    | 59.9 ms: 1.02x slower                                                    |
| mypy2                    | 226 ms                                                                     | 230 ms: 1.02x slower                                                     |
| scimark_monte_carlo      | 44.8 ms                                                                    | 45.6 ms: 1.02x slower                                                    |
| sqlglot_optimize         | 37.1 ms                                                                    | 38.0 ms: 1.02x slower                                                    |
| json                     | 2.85 ms                                                                    | 2.92 ms: 1.02x slower                                                    |
| richards_super           | 34.9 ms                                                                    | 35.8 ms: 1.02x slower                                                    |
| regex_v8                 | 13.6 ms                                                                    | 13.9 ms: 1.02x slower                                                    |
| async_generators         | 248 ms                                                                     | 254 ms: 1.03x slower                                                     |
| docutils                 | 1.71 sec                                                                   | 1.76 sec: 1.03x slower                                                   |
| dulwich_log              | 46.9 ms                                                                    | 48.2 ms: 1.03x slower                                                    |
| unpickle_pure_python     | 150 us                                                                     | 154 us: 1.03x slower                                                     |
| richards                 | 31.1 ms                                                                    | 32.0 ms: 1.03x slower                                                    |
| xml_etree_iterparse      | 66.3 ms                                                                    | 68.4 ms: 1.03x slower                                                    |
| logging_format           | 7.65 us                                                                    | 7.89 us: 1.03x slower                                                    |
| mako                     | 8.01 ms                                                                    | 8.28 ms: 1.03x slower                                                    |
| logging_simple           | 7.12 us                                                                    | 7.37 us: 1.03x slower                                                    |
| telco                    | 4.72 ms                                                                    | 4.89 ms: 1.04x slower                                                    |
| unpack_sequence          | 38.4 ns                                                                    | 39.9 ns: 1.04x slower                                                    |
| deltablue                | 2.41 ms                                                                    | 2.50 ms: 1.04x slower                                                    |
| crypto_pyaes             | 47.1 ms                                                                    | 49.0 ms: 1.04x slower                                                    |
| bench_thread_pool        | 860 us                                                                     | 894 us: 1.04x slower                                                     |
| deepcopy                 | 252 us                                                                     | 262 us: 1.04x slower                                                     |
| unpickle_list            | 2.81 us                                                                    | 2.93 us: 1.04x slower                                                    |
| spectral_norm            | 68.8 ms                                                                    | 71.7 ms: 1.04x slower                                                    |
| typing_runtime_protocols | 97.5 us                                                                    | 102 us: 1.04x slower                                                     |
| regex_compile            | 96.4 ms                                                                    | 101 ms: 1.05x slower                                                     |
| go                       | 101 ms                                                                     | 106 ms: 1.06x slower                                                     |
| pyflate                  | 327 ms                                                                     | 348 ms: 1.06x slower                                                     |
| scimark_lu               | 63.0 ms                                                                    | 67.3 ms: 1.07x slower                                                    |
| tomli_loads              | 1.65 sec                                                                   | 1.77 sec: 1.07x slower                                                   |
| mdp                      | 1.46 sec                                                                   | 1.57 sec: 1.07x slower                                                   |
| chaos                    | 44.6 ms                                                                    | 47.8 ms: 1.07x slower                                                    |
| scimark_fft              | 189 ms                                                                     | 205 ms: 1.09x slower                                                     |
| meteor_contest           | 75.4 ms                                                                    | 83.8 ms: 1.11x slower                                                    |
| deepcopy_memo            | 25.7 us                                                                    | 28.7 us: 1.12x slower                                                    |
| comprehensions           | 15.8 us                                                                    | 18.2 us: 1.15x slower                                                    |
| nqueens                  | 64.6 ms                                                                    | 74.6 ms: 1.15x slower                                                    |
| fannkuch                 | 262 ms                                                                     | 304 ms: 1.16x slower                                                     |
| hexiom                   | 4.64 ms                                                                    | 5.48 ms: 1.18x slower                                                    |
| scimark_sparse_mat_mult  | 2.60 ms                                                                    | 3.68 ms: 1.41x slower                                                    |
| Geometric mean           | (ref)                                                                      | 1.03x slower                                                             |

Benchmark hidden because not significant (17): sqlglot_transpile, create_gc_cycles, regex_dna, async_tree_none, raytrace, pprint_pformat, sqlglot_normalize, python_startup_no_site, nbody, xml_etree_process, tornado_http, dask, float, async_tree_cpu_io_mixed, async_tree_io, asyncio_tcp, asyncio_tcp_ssl
