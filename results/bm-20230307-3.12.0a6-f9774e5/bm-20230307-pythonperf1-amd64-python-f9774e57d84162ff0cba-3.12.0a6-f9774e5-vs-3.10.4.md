
# Results vs. 3.10.4

- fork: python
- ref: f9774e57d84162ff0cba
- machine: windows-amd64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 194 ms: 1.22x faster                                                       |
| chameleon      | 5.92 ms                                                     | 4.76 ms: 1.24x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.51 sec: 1.25x faster                                                     |
| html5lib       | 46.5 ms                                                     | 34.8 ms: 1.33x faster                                                      |
| tornado_http   | 109 ms                                                      | 90.6 ms: 1.20x faster                                                      |
| Geometric mean | (ref)                                                       | 1.25x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.4 ms: 1.27x faster                                                      |
| nbody          | 69.3 ms                                                     | 63.3 ms: 1.10x faster                                                      |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 83.5 ms: 1.24x faster                                                      |
| regex_dna      | 132 ms                                                      | 115 ms: 1.14x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.4 ms: 1.13x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                      |
| pickle_pure_python   | 257 us                                                      | 175 us: 1.47x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 124 us: 1.38x faster                                                       |
| xml_etree_process    | 43.4 ms                                                     | 35.6 ms: 1.22x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 88.4 ms: 1.15x faster                                                      |
| unpickle             | 9.17 us                                                     | 7.98 us: 1.15x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.05x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 52.1 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                                      |
| unpickle_list        | 2.81 us                                                     | 2.74 us: 1.03x faster                                                      |
| pickle               | 6.80 us                                                     | 6.96 us: 1.02x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.80 us: 1.08x slower                                                      |
| pickle_dict          | 16.9 us                                                     | 18.7 us: 1.11x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.20 ms: 1.42x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 13.9 ms: 1.37x faster                                                      |
| django_template | 28.2 ms                                                     | 20.9 ms: 1.35x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 30.9 ms: 1.31x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf1-amd64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.92 ms: 2.17x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 56.5 ns: 1.71x faster                                                      |
| richards                | 41.2 ms                                                     | 24.5 ms: 1.68x faster                                                      |
| mypy2                   | 352 ms                                                      | 211 ms: 1.67x faster                                                       |
| go                      | 136 ms                                                      | 82.6 ms: 1.65x faster                                                      |
| json_dumps              | 8.50 ms                                                     | 5.51 ms: 1.54x faster                                                      |
| asyncio_tcp             | 712 ms                                                      | 463 ms: 1.54x faster                                                       |
| raytrace                | 271 ms                                                      | 180 ms: 1.50x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 175 us: 1.47x faster                                                       |
| scimark_sor             | 105 ms                                                      | 71.6 ms: 1.47x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 58.7 ms: 1.46x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 3.83 ms: 1.44x faster                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 43.3 ms: 1.44x faster                                                      |
| generators              | 31.6 ms                                                     | 21.9 ms: 1.44x faster                                                      |
| pyflate                 | 387 ms                                                      | 270 ms: 1.43x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 744 ms: 1.43x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.20 ms: 1.42x faster                                                      |
| chaos                   | 58.9 ms                                                     | 42.0 ms: 1.40x faster                                                      |
| sqlglot_parse           | 1.22 ms                                                     | 871 us: 1.40x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 356 ms: 1.40x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 124 us: 1.38x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 40.4 ms: 1.38x faster                                                      |
| async_tree_none         | 420 ms                                                      | 304 ms: 1.38x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 13.9 ms: 1.37x faster                                                      |
| unpack_sequence         | 37.8 ns                                                     | 27.9 ns: 1.36x faster                                                      |
| django_template         | 28.2 ms                                                     | 20.9 ms: 1.35x faster                                                      |
| html5lib                | 46.5 ms                                                     | 34.8 ms: 1.33x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 30.9 ms: 1.31x faster                                                      |
| pycparser               | 868 ms                                                      | 663 ms: 1.31x faster                                                       |
| thrift                  | 615 us                                                      | 476 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 479 ms: 1.27x faster                                                       |
| float                   | 60.2 ms                                                     | 47.4 ms: 1.27x faster                                                      |
| deepcopy_memo           | 28.5 us                                                     | 22.6 us: 1.27x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.51 sec: 1.25x faster                                                     |
| sqlglot_optimize        | 39.0 ms                                                     | 31.2 ms: 1.25x faster                                                      |
| chameleon               | 5.92 ms                                                     | 4.76 ms: 1.24x faster                                                      |
| regex_compile           | 103 ms                                                      | 83.5 ms: 1.24x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 977 ms: 1.24x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 478 ms: 1.23x faster                                                       |
| 2to3                    | 237 ms                                                      | 194 ms: 1.22x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.6 ms: 1.22x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 168 ms: 1.21x faster                                                       |
| tornado_http            | 109 ms                                                      | 90.6 ms: 1.20x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.43 sec: 1.20x faster                                                     |
| fannkuch                | 258 ms                                                      | 216 ms: 1.20x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 56.9 ms: 1.18x faster                                                      |
| deepcopy                | 255 us                                                      | 219 us: 1.17x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 671 us: 1.17x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 67.2 ms: 1.16x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 88.4 ms: 1.15x faster                                                      |
| unpickle                | 9.17 us                                                     | 7.98 us: 1.15x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 1.88 us: 1.15x faster                                                      |
| scimark_fft             | 193 ms                                                      | 169 ms: 1.15x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 827 us: 1.14x faster                                                       |
| regex_dna               | 132 ms                                                      | 115 ms: 1.14x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                      |
| sympy_expand            | 315 ms                                                      | 277 ms: 1.14x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 42.2 ms: 1.13x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.4 ms: 1.13x faster                                                      |
| json                    | 3.05 ms                                                     | 2.74 ms: 1.11x faster                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.2 ms: 1.10x faster                                                      |
| nbody                   | 69.3 ms                                                     | 63.3 ms: 1.10x faster                                                      |
| sympy_str               | 188 ms                                                      | 173 ms: 1.09x faster                                                       |
| sympy_sum               | 104 ms                                                      | 96.6 ms: 1.08x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 68.0 ms: 1.07x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.4 us: 1.05x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 73.9 ms: 1.05x faster                                                      |
| xml_etree_generate      | 54.5 ms                                                     | 52.1 ms: 1.05x faster                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.56 ms: 1.04x faster                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.79 us: 1.03x faster                                                      |
| unpickle_list           | 2.81 us                                                     | 2.74 us: 1.03x faster                                                      |
| logging_format          | 6.66 us                                                     | 6.55 us: 1.02x faster                                                      |
| logging_simple          | 6.20 us                                                     | 6.10 us: 1.02x faster                                                      |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.86 ms: 1.02x slower                                                      |
| pickle                  | 6.80 us                                                     | 6.96 us: 1.02x slower                                                      |
| bench_mp_pool           | 60.7 ms                                                     | 63.1 ms: 1.04x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.44 ms: 1.07x slower                                                      |
| pickle_list             | 2.59 us                                                     | 2.80 us: 1.08x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 18.7 us: 1.11x slower                                                      |
| dask                    | 305 ms                                                      | 352 ms: 1.16x slower                                                       |
| coverage                | 40.0 ms                                                     | 49.9 ms: 1.25x slower                                                      |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                               |

Benchmark hidden because not significant (3): comprehensions, async_generators, python_startup_no_site
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
