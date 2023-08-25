
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: windows-amd64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 193 ms: 1.23x faster                                                       |
| chameleon      | 5.92 ms                                                     | 4.39 ms: 1.35x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.48 sec: 1.28x faster                                                     |
| html5lib       | 46.5 ms                                                     | 33.7 ms: 1.38x faster                                                      |
| Geometric mean | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.2 ms: 1.27x faster                                                      |
| nbody          | 69.3 ms                                                     | 59.5 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.8 ms: 1.31x faster                                                      |
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.10 ms: 1.67x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 169 us: 1.52x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 119 us: 1.44x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 33.8 ms: 1.28x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 86.5 ms: 1.18x faster                                                      |
| json_loads           | 14.2 us                                                     | 12.4 us: 1.14x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 48.3 ms: 1.13x faster                                                      |
| unpickle_list        | 2.81 us                                                     | 2.59 us: 1.09x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 60.1 ms: 1.06x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.70 us: 1.05x faster                                                      |
| pickle               | 6.80 us                                                     | 6.55 us: 1.04x faster                                                      |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.81 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.1 ms: 1.10x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.05 ms: 1.45x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 13.3 ms: 1.44x faster                                                      |
| django_template | 28.2 ms                                                     | 20.7 ms: 1.37x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.40x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf1-amd64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.94 ms: 2.15x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 54.2 ns: 1.78x faster                                                      |
| richards                | 41.2 ms                                                     | 24.0 ms: 1.72x faster                                                      |
| go                      | 136 ms                                                      | 80.4 ms: 1.69x faster                                                      |
| mypy2                   | 352 ms                                                      | 209 ms: 1.68x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.10 ms: 1.67x faster                                                      |
| scimark_sor             | 105 ms                                                      | 63.7 ms: 1.65x faster                                                      |
| raytrace                | 271 ms                                                      | 171 ms: 1.58x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 466 ms: 1.53x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 56.0 ms: 1.53x faster                                                      |
| pickle_pure_python      | 257 us                                                      | 169 us: 1.52x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 38.0 ms: 1.47x faster                                                      |
| pyflate                 | 387 ms                                                      | 263 ms: 1.47x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.77 ms: 1.46x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 342 ms: 1.46x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.05 ms: 1.45x faster                                                      |
| unpack_sequence         | 37.8 ns                                                     | 26.2 ns: 1.44x faster                                                      |
| sqlglot_parse           | 1.22 ms                                                     | 848 us: 1.44x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.3 ms: 1.44x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 742 ms: 1.44x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 119 us: 1.44x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.02 ms: 1.43x faster                                                      |
| async_tree_none         | 420 ms                                                      | 295 ms: 1.42x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 20.4 us: 1.40x faster                                                      |
| chaos                   | 58.9 ms                                                     | 42.1 ms: 1.40x faster                                                      |
| pycparser               | 868 ms                                                      | 628 ms: 1.38x faster                                                       |
| html5lib                | 46.5 ms                                                     | 33.7 ms: 1.38x faster                                                      |
| django_template         | 28.2 ms                                                     | 20.7 ms: 1.37x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 45.9 ms: 1.36x faster                                                      |
| chameleon               | 5.92 ms                                                     | 4.39 ms: 1.35x faster                                                      |
| thrift                  | 615 us                                                      | 463 us: 1.33x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                                      |
| async_generators        | 224 ms                                                      | 169 ms: 1.32x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 918 ms: 1.31x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 448 ms: 1.31x faster                                                       |
| regex_compile           | 103 ms                                                      | 78.8 ms: 1.31x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 465 ms: 1.31x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 33.8 ms: 1.28x faster                                                      |
| deepcopy                | 255 us                                                      | 199 us: 1.28x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.48 sec: 1.28x faster                                                     |
| float                   | 60.2 ms                                                     | 47.2 ms: 1.27x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 30.6 ms: 1.27x faster                                                      |
| spectral_norm           | 78.0 ms                                                     | 62.8 ms: 1.24x faster                                                      |
| dask                    | 305 ms                                                      | 246 ms: 1.24x faster                                                       |
| 2to3                    | 237 ms                                                      | 193 ms: 1.23x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.78 us: 1.21x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 168 ms: 1.20x faster                                                       |
| fannkuch                | 258 ms                                                      | 217 ms: 1.19x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 40.1 ms: 1.19x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 798 us: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.25 ms: 1.18x faster                                                      |
| create_gc_cycles        | 782 us                                                      | 661 us: 1.18x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.6 ms: 1.18x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 86.5 ms: 1.18x faster                                                      |
| sympy_expand            | 315 ms                                                      | 269 ms: 1.17x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 57.3 ms: 1.17x faster                                                      |
| json                    | 3.05 ms                                                     | 2.61 ms: 1.17x faster                                                      |
| nbody                   | 69.3 ms                                                     | 59.5 ms: 1.17x faster                                                      |
| scimark_fft             | 193 ms                                                      | 167 ms: 1.16x faster                                                       |
| coroutines              | 15.9 ms                                                     | 13.9 ms: 1.15x faster                                                      |
| json_loads              | 14.2 us                                                     | 12.4 us: 1.14x faster                                                      |
| sympy_sum               | 104 ms                                                      | 92.0 ms: 1.13x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.51 sec: 1.13x faster                                                     |
| xml_etree_generate      | 54.5 ms                                                     | 48.3 ms: 1.13x faster                                                      |
| sympy_str               | 188 ms                                                      | 168 ms: 1.12x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.1 ms: 1.10x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                      |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.59 us: 1.09x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.72 us: 1.07x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 67.9 ms: 1.07x faster                                                      |
| comprehensions          | 16.0 us                                                     | 15.0 us: 1.06x faster                                                      |
| logging_simple          | 6.20 us                                                     | 5.84 us: 1.06x faster                                                      |
| logging_format          | 6.66 us                                                     | 6.29 us: 1.06x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 73.2 ms: 1.06x faster                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 60.1 ms: 1.06x faster                                                      |
| unpickle                | 9.17 us                                                     | 8.70 us: 1.05x faster                                                      |
| telco                   | 3.78 ms                                                     | 3.59 ms: 1.05x faster                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.55 us: 1.04x faster                                                      |
| python_startup_no_site  | 15.5 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 61.1 ms: 1.01x slower                                                      |
| generators              | 31.6 ms                                                     | 33.1 ms: 1.05x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.43 ms: 1.07x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.2 us: 1.08x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.81 us: 1.09x slower                                                      |
| coverage                | 40.0 ms                                                     | 52.5 ms: 1.31x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x
