
# Results vs. 3.10.4

- fork: python
- ref: 3b9d793efcfd2c00c14f
- machine: windows-amd64
- commit hash: 3b9d793
- commit date: 2022-11-14
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 193 ms: 1.23x faster                                                       |
| chameleon      | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.52 sec: 1.25x faster                                                     |
| html5lib       | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                      |
| tornado_http   | 109 ms                                                      | 89.5 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.7 ms: 1.24x faster                                                      |
| nbody          | 69.3 ms                                                     | 62.3 ms: 1.11x faster                                                      |
| pidigits       | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 82.3 ms: 1.26x faster                                                      |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                       | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.12 ms: 1.66x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 180 us: 1.42x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 130 us: 1.31x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 87.6 ms: 1.16x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 49.0 ms: 1.11x faster                                                      |
| unpickle             | 9.17 us                                                     | 8.25 us: 1.11x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.07x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                                      |
| pickle               | 6.80 us                                                     | 6.57 us: 1.03x faster                                                      |
| pickle_list          | 2.59 us                                                     | 2.62 us: 1.01x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.3 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.25 ms: 1.41x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                      |
| django_template | 28.2 ms                                                     | 21.6 ms: 1.31x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 32.2 ms: 1.26x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221114-pythonperf1-amd64-python-3b9d793efcfd2c00c14f-3.12.0a2-3b9d793 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.24 ms: 1.86x faster                                                      |
| mypy2                   | 352 ms                                                      | 212 ms: 1.66x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.12 ms: 1.66x faster                                                      |
| go                      | 136 ms                                                      | 84.0 ms: 1.62x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 59.9 ns: 1.61x faster                                                      |
| richards                | 41.2 ms                                                     | 26.7 ms: 1.54x faster                                                      |
| scimark_sor             | 105 ms                                                      | 69.2 ms: 1.52x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 56.9 ms: 1.50x faster                                                      |
| raytrace                | 271 ms                                                      | 184 ms: 1.47x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 180 us: 1.42x faster                                                       |
| pyflate                 | 387 ms                                                      | 272 ms: 1.42x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 865 us: 1.41x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.25 ms: 1.41x faster                                                      |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.8 ms: 1.40x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 4.00 ms: 1.38x faster                                                      |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 45.4 ms: 1.37x faster                                                      |
| chaos                   | 58.9 ms                                                     | 43.1 ms: 1.37x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 783 ms: 1.36x faster                                                       |
| pycparser               | 868 ms                                                      | 650 ms: 1.33x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 130 us: 1.31x faster                                                       |
| django_template         | 28.2 ms                                                     | 21.6 ms: 1.31x faster                                                      |
| async_generators        | 224 ms                                                      | 173 ms: 1.29x faster                                                       |
| async_tree_none         | 420 ms                                                      | 325 ms: 1.29x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 934 ms: 1.29x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.59 ms: 1.29x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 458 ms: 1.29x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 22.2 us: 1.28x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 33.9 ms: 1.28x faster                                                      |
| html5lib                | 46.5 ms                                                     | 36.4 ms: 1.28x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 32.2 ms: 1.26x faster                                                      |
| regex_compile           | 103 ms                                                      | 82.3 ms: 1.26x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.52 sec: 1.25x faster                                                     |
| float                   | 60.2 ms                                                     | 48.7 ms: 1.24x faster                                                      |
| spectral_norm           | 78.0 ms                                                     | 63.1 ms: 1.24x faster                                                      |
| 2to3                    | 237 ms                                                      | 193 ms: 1.23x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 30.8 ns: 1.23x faster                                                      |
| tornado_http            | 109 ms                                                      | 89.5 ms: 1.22x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 32.1 ms: 1.21x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 507 ms: 1.20x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.25 ms: 1.18x faster                                                      |
| dask                    | 305 ms                                                      | 258 ms: 1.18x faster                                                       |
| deepcopy                | 255 us                                                      | 217 us: 1.18x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 665 us: 1.18x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 57.5 ms: 1.17x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 87.6 ms: 1.16x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 174 ms: 1.16x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.87 us: 1.15x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 12.9 ms: 1.15x faster                                                      |
| scimark_fft             | 193 ms                                                      | 170 ms: 1.14x faster                                                       |
| fannkuch                | 258 ms                                                      | 227 ms: 1.14x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 835 us: 1.13x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.53 sec: 1.12x faster                                                     |
| sympy_expand            | 315 ms                                                      | 282 ms: 1.12x faster                                                       |
| nbody                   | 69.3 ms                                                     | 62.3 ms: 1.11x faster                                                      |
| xml_etree_generate      | 54.5 ms                                                     | 49.0 ms: 1.11x faster                                                      |
| unpickle                | 9.17 us                                                     | 8.25 us: 1.11x faster                                                      |
| json                    | 3.05 ms                                                     | 2.75 ms: 1.11x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 43.1 ms: 1.10x faster                                                      |
| thrift                  | 615 us                                                      | 558 us: 1.10x faster                                                       |
| regex_dna               | 132 ms                                                      | 120 ms: 1.10x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                      |
| sympy_sum               | 104 ms                                                      | 96.1 ms: 1.08x faster                                                      |
| sympy_str               | 188 ms                                                      | 175 ms: 1.08x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.71 us: 1.07x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.07x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 72.6 ms: 1.07x faster                                                      |
| coroutines              | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 69.3 ms: 1.05x faster                                                      |
| comprehensions          | 16.0 us                                                     | 15.4 us: 1.04x faster                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                                      |
| pickle                  | 6.80 us                                                     | 6.57 us: 1.03x faster                                                      |
| logging_format          | 6.66 us                                                     | 6.56 us: 1.02x faster                                                      |
| pidigits                | 145 ms                                                      | 146 ms: 1.01x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 61.2 ms: 1.01x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.62 us: 1.01x slower                                                      |
| logging_simple          | 6.20 us                                                     | 6.31 us: 1.02x slower                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.70 ms: 1.02x slower                                                      |
| telco                   | 3.78 ms                                                     | 3.95 ms: 1.04x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.44 ms: 1.07x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.3 us: 1.08x slower                                                      |
| generators              | 31.6 ms                                                     | 35.7 ms: 1.13x slower                                                      |
| coverage                | 40.0 ms                                                     | 52.0 ms: 1.30x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (3): unpickle_list, python_startup_no_site, asyncio_tcp
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x
