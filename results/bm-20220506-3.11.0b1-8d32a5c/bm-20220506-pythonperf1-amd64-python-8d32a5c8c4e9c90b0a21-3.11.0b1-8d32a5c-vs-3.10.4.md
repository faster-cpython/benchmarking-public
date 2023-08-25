
# Results vs. 3.10.4

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: windows-amd64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 203 ms: 1.17x faster                                                       |
| chameleon      | 5.92 ms                                                     | 5.45 ms: 1.09x faster                                                      |
| docutils       | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                     |
| html5lib       | 46.5 ms                                                     | 38.3 ms: 1.21x faster                                                      |
| tornado_http   | 109 ms                                                      | 89.7 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.5 ms: 1.13x faster                                                      |
| nbody          | 69.3 ms                                                     | 67.9 ms: 1.02x faster                                                      |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 90.5 ms: 1.14x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 257 us                                                      | 204 us: 1.26x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.87 us: 1.17x faster                                                      |
| xml_etree_process    | 43.4 ms                                                     | 37.6 ms: 1.16x faster                                                      |
| unpickle_pure_python | 171 us                                                      | 152 us: 1.12x faster                                                       |
| json_dumps           | 8.50 ms                                                     | 7.72 ms: 1.10x faster                                                      |
| xml_etree_parse      | 102 ms                                                      | 93.1 ms: 1.09x faster                                                      |
| unpickle_list        | 2.81 us                                                     | 2.58 us: 1.09x faster                                                      |
| json_loads           | 14.2 us                                                     | 13.4 us: 1.06x faster                                                      |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.1 ms: 1.04x faster                                                      |
| pickle               | 6.80 us                                                     | 6.59 us: 1.03x faster                                                      |
| xml_etree_generate   | 54.5 ms                                                     | 53.0 ms: 1.03x faster                                                      |
| pickle_dict          | 16.9 us                                                     | 17.1 us: 1.01x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.67 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                      |
| python_startup_no_site | 15.5 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.13 ms: 1.23x faster                                                      |
| django_template | 28.2 ms                                                     | 24.0 ms: 1.18x faster                                                      |
| genshi_text     | 19.0 ms                                                     | 17.7 ms: 1.08x faster                                                      |
| genshi_xml      | 40.5 ms                                                     | 39.8 ms: 1.02x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.66 ms: 1.57x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 751 ms: 1.42x faster                                                       |
| go                      | 136 ms                                                      | 97.9 ms: 1.39x faster                                                      |
| logging_silent          | 96.4 ns                                                     | 70.2 ns: 1.37x faster                                                      |
| richards                | 41.2 ms                                                     | 30.1 ms: 1.37x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 62.7 ms: 1.36x faster                                                      |
| scimark_sor             | 105 ms                                                      | 77.1 ms: 1.36x faster                                                      |
| async_tree_none         | 420 ms                                                      | 311 ms: 1.35x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 370 ms: 1.35x faster                                                       |
| raytrace                | 271 ms                                                      | 203 ms: 1.33x faster                                                       |
| pyflate                 | 387 ms                                                      | 303 ms: 1.28x faster                                                       |
| mypy2                   | 352 ms                                                      | 277 ms: 1.27x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 49.1 ms: 1.27x faster                                                      |
| pickle_pure_python      | 257 us                                                      | 204 us: 1.26x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 45.0 ms: 1.24x faster                                                      |
| mako                    | 8.80 ms                                                     | 7.13 ms: 1.23x faster                                                      |
| async_generators        | 224 ms                                                      | 182 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 499 ms: 1.22x faster                                                       |
| thrift                  | 615 us                                                      | 504 us: 1.22x faster                                                       |
| tornado_http            | 109 ms                                                      | 89.7 ms: 1.22x faster                                                      |
| html5lib                | 46.5 ms                                                     | 38.3 ms: 1.21x faster                                                      |
| docutils                | 1.89 sec                                                    | 1.57 sec: 1.20x faster                                                     |
| chaos                   | 58.9 ms                                                     | 48.9 ms: 1.20x faster                                                      |
| hexiom                  | 5.52 ms                                                     | 4.59 ms: 1.20x faster                                                      |
| aiohttp                 | 1.01 ms                                                     | 854 us: 1.18x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 663 us: 1.18x faster                                                       |
| django_template         | 28.2 ms                                                     | 24.0 ms: 1.18x faster                                                      |
| unpickle                | 9.17 us                                                     | 7.87 us: 1.17x faster                                                      |
| 2to3                    | 237 ms                                                      | 203 ms: 1.17x faster                                                       |
| pycparser               | 868 ms                                                      | 748 ms: 1.16x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.6 ms: 1.16x faster                                                      |
| regex_compile           | 103 ms                                                      | 90.5 ms: 1.14x faster                                                      |
| deepcopy_memo           | 28.5 us                                                     | 25.1 us: 1.14x faster                                                      |
| dask                    | 305 ms                                                      | 268 ms: 1.14x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| float                   | 60.2 ms                                                     | 53.5 ms: 1.13x faster                                                      |
| unpickle_pure_python    | 171 us                                                      | 152 us: 1.12x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 525 ms: 1.12x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 69.6 ms: 1.12x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.08 sec: 1.12x faster                                                     |
| pylint                  | 347 ms                                                      | 314 ms: 1.11x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 7.72 ms: 1.10x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 35.6 ms: 1.09x faster                                                      |
| xml_etree_parse         | 102 ms                                                      | 93.1 ms: 1.09x faster                                                      |
| unpickle_list           | 2.81 us                                                     | 2.58 us: 1.09x faster                                                      |
| sqlite_synth            | 1.84 us                                                     | 1.69 us: 1.09x faster                                                      |
| sympy_integrate         | 14.8 ms                                                     | 13.6 ms: 1.09x faster                                                      |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                       |
| chameleon               | 5.92 ms                                                     | 5.45 ms: 1.09x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.4 ms: 1.09x faster                                                      |
| pathlib                 | 77.4 ms                                                     | 71.4 ms: 1.08x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.9 ms: 1.08x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 17.7 ms: 1.08x faster                                                      |
| sympy_expand            | 315 ms                                                      | 293 ms: 1.08x faster                                                       |
| scimark_fft             | 193 ms                                                      | 180 ms: 1.07x faster                                                       |
| sympy_sum               | 104 ms                                                      | 96.9 ms: 1.07x faster                                                      |
| sqlglot_transpile       | 1.46 ms                                                     | 1.37 ms: 1.07x faster                                                      |
| logging_simple          | 6.20 us                                                     | 5.80 us: 1.07x faster                                                      |
| bench_thread_pool       | 946 us                                                      | 888 us: 1.07x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.25 us: 1.07x faster                                                      |
| asyncio_tcp             | 712 ms                                                      | 673 ms: 1.06x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 1.15 ms: 1.06x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.4 us: 1.06x faster                                                      |
| coroutines              | 15.9 ms                                                     | 15.2 ms: 1.05x faster                                                      |
| mdp                     | 1.71 sec                                                    | 1.63 sec: 1.05x faster                                                     |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.1 ms: 1.04x faster                                                      |
| sqlglot_normalize       | 202 ms                                                      | 196 ms: 1.03x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.59 us: 1.03x faster                                                      |
| sympy_str               | 188 ms                                                      | 183 ms: 1.03x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 53.0 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.60 ms: 1.02x faster                                                      |
| fannkuch                | 258 ms                                                      | 252 ms: 1.02x faster                                                       |
| nbody                   | 69.3 ms                                                     | 67.9 ms: 1.02x faster                                                      |
| python_startup_no_site  | 15.5 ms                                                     | 15.2 ms: 1.02x faster                                                      |
| genshi_xml              | 40.5 ms                                                     | 39.8 ms: 1.02x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 2.12 us: 1.02x faster                                                      |
| deepcopy                | 255 us                                                      | 252 us: 1.01x faster                                                       |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                     |
| nqueens                 | 67.0 ms                                                     | 67.6 ms: 1.01x slower                                                      |
| pickle_dict             | 16.9 us                                                     | 17.1 us: 1.01x slower                                                      |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.67 us: 1.03x slower                                                      |
| meteor_contest          | 72.5 ms                                                     | 75.5 ms: 1.04x slower                                                      |
| telco                   | 3.78 ms                                                     | 3.94 ms: 1.04x slower                                                      |
| gc_traversal            | 1.34 ms                                                     | 1.42 ms: 1.05x slower                                                      |
| json                    | 3.05 ms                                                     | 3.25 ms: 1.07x slower                                                      |
| generators              | 31.6 ms                                                     | 33.9 ms: 1.07x slower                                                      |
| comprehensions          | 16.0 us                                                     | 17.8 us: 1.11x slower                                                      |
| unpack_sequence         | 37.8 ns                                                     | 42.2 ns: 1.11x slower                                                      |
| coverage                | 40.0 ms                                                     | 103 ms: 2.56x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x
