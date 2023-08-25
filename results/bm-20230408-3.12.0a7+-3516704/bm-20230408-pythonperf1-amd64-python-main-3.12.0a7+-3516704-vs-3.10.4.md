
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 207 ms: 1.15x faster                                        |
| chameleon      | 5.92 ms                                                     | 4.62 ms: 1.28x faster                                       |
| docutils       | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                      |
| html5lib       | 46.5 ms                                                     | 36.7 ms: 1.27x faster                                       |
| tornado_http   | 109 ms                                                      | 89.7 ms: 1.22x faster                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 60.2 ms                                                     | 48.1 ms: 1.25x faster                                       |
| nbody          | 69.3 ms                                                     | 56.5 ms: 1.23x faster                                       |
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 83.5 ms: 1.24x faster                                       |
| regex_v8       | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                       |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                       |
| regex_dna      | 132 ms                                                      | 123 ms: 1.08x faster                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.39 ms: 1.58x faster                                       |
| pickle_pure_python   | 257 us                                                      | 184 us: 1.39x faster                                        |
| unpickle_pure_python | 171 us                                                      | 127 us: 1.34x faster                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.2 ms: 1.23x faster                                       |
| xml_etree_parse      | 102 ms                                                      | 89.9 ms: 1.13x faster                                       |
| unpickle             | 9.17 us                                                     | 8.29 us: 1.11x faster                                       |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| unpickle_list        | 2.81 us                                                     | 2.74 us: 1.03x faster                                       |
| pickle               | 6.80 us                                                     | 6.93 us: 1.02x slower                                       |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                       |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.07x faster                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.22 ms: 1.42x faster                                       |
| genshi_text     | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                       |
| django_template | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                       |
| genshi_xml      | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.94 ms: 2.15x faster                                       |
| logging_silent          | 96.4 ns                                                     | 54.4 ns: 1.77x faster                                       |
| richards                | 41.2 ms                                                     | 25.2 ms: 1.63x faster                                       |
| sqlglot_parse           | 1.22 ms                                                     | 747 us: 1.63x faster                                        |
| go                      | 136 ms                                                      | 83.8 ms: 1.63x faster                                       |
| mypy2                   | 352 ms                                                      | 219 ms: 1.61x faster                                        |
| scimark_lu              | 85.4 ms                                                     | 53.8 ms: 1.59x faster                                       |
| json_dumps              | 8.50 ms                                                     | 5.39 ms: 1.58x faster                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 947 us: 1.55x faster                                        |
| raytrace                | 271 ms                                                      | 176 ms: 1.54x faster                                        |
| generators              | 31.6 ms                                                     | 20.7 ms: 1.53x faster                                       |
| asyncio_tcp             | 712 ms                                                      | 487 ms: 1.46x faster                                        |
| hexiom                  | 5.52 ms                                                     | 3.87 ms: 1.42x faster                                       |
| scimark_sor             | 105 ms                                                      | 73.7 ms: 1.42x faster                                       |
| mako                    | 8.80 ms                                                     | 6.22 ms: 1.42x faster                                       |
| async_tree_io           | 1.07 sec                                                    | 760 ms: 1.40x faster                                        |
| pickle_pure_python      | 257 us                                                      | 184 us: 1.39x faster                                        |
| chaos                   | 58.9 ms                                                     | 42.6 ms: 1.38x faster                                       |
| genshi_text             | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                       |
| crypto_pyaes            | 62.3 ms                                                     | 46.0 ms: 1.35x faster                                       |
| pyflate                 | 387 ms                                                      | 287 ms: 1.35x faster                                        |
| unpickle_pure_python    | 171 us                                                      | 127 us: 1.34x faster                                        |
| async_tree_memoization  | 497 ms                                                      | 370 ms: 1.34x faster                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.6 ms: 1.34x faster                                       |
| deepcopy_memo           | 28.5 us                                                     | 21.3 us: 1.34x faster                                       |
| unpack_sequence         | 37.8 ns                                                     | 28.2 ns: 1.34x faster                                       |
| django_template         | 28.2 ms                                                     | 21.1 ms: 1.34x faster                                       |
| async_tree_none         | 420 ms                                                      | 314 ms: 1.34x faster                                        |
| genshi_xml              | 40.5 ms                                                     | 30.5 ms: 1.33x faster                                       |
| pycparser               | 868 ms                                                      | 655 ms: 1.32x faster                                        |
| thrift                  | 615 us                                                      | 473 us: 1.30x faster                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 470 ms: 1.30x faster                                        |
| spectral_norm           | 78.0 ms                                                     | 60.4 ms: 1.29x faster                                       |
| chameleon               | 5.92 ms                                                     | 4.62 ms: 1.28x faster                                       |
| html5lib                | 46.5 ms                                                     | 36.7 ms: 1.27x faster                                       |
| pprint_safe_repr        | 589 ms                                                      | 467 ms: 1.26x faster                                        |
| pprint_pformat          | 1.21 sec                                                    | 963 ms: 1.25x faster                                        |
| float                   | 60.2 ms                                                     | 48.1 ms: 1.25x faster                                       |
| regex_compile           | 103 ms                                                      | 83.5 ms: 1.24x faster                                       |
| xml_etree_process       | 43.4 ms                                                     | 35.2 ms: 1.23x faster                                       |
| mdp                     | 1.71 sec                                                    | 1.39 sec: 1.23x faster                                      |
| nbody                   | 69.3 ms                                                     | 56.5 ms: 1.23x faster                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 32.0 ms: 1.22x faster                                       |
| tornado_http            | 109 ms                                                      | 89.7 ms: 1.22x faster                                       |
| docutils                | 1.89 sec                                                    | 1.56 sec: 1.21x faster                                      |
| nqueens                 | 67.0 ms                                                     | 56.4 ms: 1.19x faster                                       |
| scimark_fft             | 193 ms                                                      | 164 ms: 1.18x faster                                        |
| coroutines              | 15.9 ms                                                     | 13.6 ms: 1.17x faster                                       |
| deepcopy                | 255 us                                                      | 218 us: 1.17x faster                                        |
| sqlglot_normalize       | 202 ms                                                      | 174 ms: 1.16x faster                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.29 ms: 1.16x faster                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                       |
| 2to3                    | 237 ms                                                      | 207 ms: 1.15x faster                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.89 us: 1.14x faster                                       |
| regex_v8                | 15.0 ms                                                     | 13.2 ms: 1.14x faster                                       |
| create_gc_cycles        | 782 us                                                      | 688 us: 1.14x faster                                        |
| xml_etree_parse         | 102 ms                                                      | 89.9 ms: 1.13x faster                                       |
| sympy_expand            | 315 ms                                                      | 279 ms: 1.13x faster                                        |
| comprehensions          | 16.0 us                                                     | 14.2 us: 1.13x faster                                       |
| dulwich_log             | 47.6 ms                                                     | 42.3 ms: 1.12x faster                                       |
| json                    | 3.05 ms                                                     | 2.72 ms: 1.12x faster                                       |
| bench_thread_pool       | 946 us                                                      | 852 us: 1.11x faster                                        |
| unpickle                | 9.17 us                                                     | 8.29 us: 1.11x faster                                       |
| fannkuch                | 258 ms                                                      | 236 ms: 1.09x faster                                        |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                       |
| regex_effbot            | 1.66 ms                                                     | 1.53 ms: 1.09x faster                                       |
| sympy_str               | 188 ms                                                      | 174 ms: 1.08x faster                                        |
| regex_dna               | 132 ms                                                      | 123 ms: 1.08x faster                                        |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.07x faster                                       |
| async_generators        | 224 ms                                                      | 211 ms: 1.06x faster                                        |
| sympy_sum               | 104 ms                                                      | 98.4 ms: 1.06x faster                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.7 ms: 1.05x faster                                       |
| logging_simple          | 6.20 us                                                     | 5.94 us: 1.04x faster                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.3 ms: 1.04x faster                                       |
| meteor_contest          | 72.5 ms                                                     | 70.5 ms: 1.03x faster                                       |
| unpickle_list           | 2.81 us                                                     | 2.74 us: 1.03x faster                                       |
| logging_format          | 6.66 us                                                     | 6.55 us: 1.02x faster                                       |
| sqlite_synth            | 1.84 us                                                     | 1.87 us: 1.01x slower                                       |
| pickle                  | 6.80 us                                                     | 6.93 us: 1.02x slower                                       |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                        |
| telco                   | 3.78 ms                                                     | 3.90 ms: 1.03x slower                                       |
| python_startup_no_site  | 15.5 ms                                                     | 16.1 ms: 1.04x slower                                       |
| pickle_list             | 2.59 us                                                     | 2.82 us: 1.09x slower                                       |
| bench_mp_pool           | 60.7 ms                                                     | 67.1 ms: 1.11x slower                                       |
| pathlib                 | 77.4 ms                                                     | 85.9 ms: 1.11x slower                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.13x slower                                       |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                       |
| dask                    | 305 ms                                                      | 360 ms: 1.18x slower                                        |
| coverage                | 40.0 ms                                                     | 50.8 ms: 1.27x slower                                       |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
