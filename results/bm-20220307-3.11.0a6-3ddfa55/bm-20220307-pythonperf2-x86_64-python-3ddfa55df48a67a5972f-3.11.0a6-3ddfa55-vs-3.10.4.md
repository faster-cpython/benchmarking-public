
# Results vs. 3.10.4

- fork: python
- ref: 3ddfa55df48a67a5972f
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.14x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 300 ms: 1.17x faster                                                        |
| chameleon      | 9.72 ms                                                      | 8.43 ms: 1.15x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.98 sec: 1.14x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.6 ms: 1.25x faster                                                       |
| tornado_http   | 152 ms                                                       | 130 ms: 1.17x faster                                                        |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 98.0 ms: 1.40x faster                                                       |
| float          | 110 ms                                                       | 79.1 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 161 ms: 1.20x faster                                                        |
| regex_dna      | 259 ms                                                       | 257 ms: 1.01x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 26.4 ms: 1.01x faster                                                       |
| regex_effbot   | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                       | 352 us: 1.30x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 59.4 ms: 1.28x faster                                                       |
| json_loads           | 30.0 us                                                      | 23.9 us: 1.25x faster                                                       |
| unpickle_pure_python | 321 us                                                       | 273 us: 1.18x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.5 us: 1.05x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 154 ms: 1.05x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 13.6 ms: 1.04x faster                                                       |
| pickle               | 9.94 us                                                      | 9.96 us: 1.00x slower                                                       |
| unpickle_list        | 4.49 us                                                      | 4.68 us: 1.04x slower                                                       |
| pickle_list          | 4.11 us                                                      | 4.28 us: 1.04x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 32.2 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.4 ms: 1.10x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.55 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| django_template | 51.5 ms                                                      | 43.8 ms: 1.18x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 60.7 ms: 1.07x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220307-pythonperf2-x86_64-python-3ddfa55df48a67a5972f-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 4.49 ms: 1.66x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 4.80 ms: 1.49x faster                                                       |
| scimark_monte_carlo     | 109 ms                                                       | 74.4 ms: 1.47x faster                                                       |
| scimark_sor             | 177 ms                                                       | 121 ms: 1.46x faster                                                        |
| go                      | 259 ms                                                       | 178 ms: 1.46x faster                                                        |
| logging_silent          | 166 ns                                                       | 115 ns: 1.44x faster                                                        |
| raytrace                | 488 ms                                                       | 343 ms: 1.42x faster                                                        |
| pyflate                 | 697 ms                                                       | 494 ms: 1.41x faster                                                        |
| nbody                   | 137 ms                                                       | 98.0 ms: 1.40x faster                                                       |
| float                   | 110 ms                                                       | 79.1 ms: 1.39x faster                                                       |
| chaos                   | 107 ms                                                       | 77.5 ms: 1.38x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.19 sec: 1.35x faster                                                      |
| scimark_lu              | 164 ms                                                       | 122 ms: 1.35x faster                                                        |
| richards                | 74.1 ms                                                      | 55.9 ms: 1.33x faster                                                       |
| async_generators        | 422 ms                                                       | 320 ms: 1.32x faster                                                        |
| async_tree_none         | 700 ms                                                       | 532 ms: 1.32x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 352 us: 1.30x faster                                                        |
| mako                    | 14.7 ms                                                      | 11.4 ms: 1.28x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 59.4 ms: 1.28x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 651 ms: 1.27x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 93.5 ms: 1.26x faster                                                       |
| logging_simple          | 8.90 us                                                      | 7.08 us: 1.26x faster                                                       |
| json_loads              | 30.0 us                                                      | 23.9 us: 1.25x faster                                                       |
| html5lib                | 94.6 ms                                                      | 75.6 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 763 ms: 1.25x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.75 us: 1.23x faster                                                       |
| spectral_norm           | 136 ms                                                       | 111 ms: 1.23x faster                                                        |
| pprint_safe_repr        | 1.05 sec                                                     | 853 ms: 1.23x faster                                                        |
| hexiom                  | 9.52 ms                                                      | 7.74 ms: 1.23x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.77 sec: 1.22x faster                                                      |
| aiohttp                 | 1.21 ms                                                      | 1.00 ms: 1.21x faster                                                       |
| regex_compile           | 194 ms                                                       | 161 ms: 1.20x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 26.5 ms: 1.19x faster                                                       |
| json                    | 5.96 ms                                                      | 5.04 ms: 1.18x faster                                                       |
| gunicorn                | 1.17 ms                                                      | 994 us: 1.18x faster                                                        |
| scimark_fft             | 359 ms                                                       | 305 ms: 1.18x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 273 us: 1.18x faster                                                        |
| django_template         | 51.5 ms                                                      | 43.8 ms: 1.18x faster                                                       |
| thrift                  | 1.16 ms                                                      | 991 us: 1.17x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 41.7 us: 1.17x faster                                                       |
| tornado_http            | 152 ms                                                       | 130 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.54 us: 1.17x faster                                                       |
| 2to3                    | 350 ms                                                       | 300 ms: 1.17x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.43 sec: 1.16x faster                                                      |
| chameleon               | 9.72 ms                                                      | 8.43 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.53 ms: 1.15x faster                                                       |
| docutils                | 3.40 sec                                                     | 2.98 sec: 1.14x faster                                                      |
| sqlalchemy_declarative  | 187 ms                                                       | 164 ms: 1.14x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 19.3 ms: 1.12x faster                                                       |
| nqueens                 | 112 ms                                                       | 100 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 63.7 ms: 1.10x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 131 ms: 1.10x faster                                                        |
| python_startup          | 11.5 ms                                                      | 10.4 ms: 1.10x faster                                                       |
| deepcopy                | 454 us                                                       | 413 us: 1.10x faster                                                        |
| flaskblogging           | 4.39 ms                                                      | 3.99 ms: 1.10x faster                                                       |
| fannkuch                | 496 ms                                                       | 453 ms: 1.10x faster                                                        |
| bench_thread_pool       | 1.14 ms                                                      | 1.04 ms: 1.09x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 73.8 ms: 1.08x faster                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 2.50 ms: 1.08x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.9 ms: 1.08x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.73 us: 1.08x faster                                                       |
| sqlalchemy_imperative   | 22.6 ms                                                      | 21.0 ms: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 60.7 ms: 1.07x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 2.13 ms: 1.06x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| generators              | 58.0 ms                                                      | 54.8 ms: 1.06x faster                                                       |
| unpickle                | 14.2 us                                                      | 13.5 us: 1.05x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 154 ms: 1.05x faster                                                        |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| dask                    | 463 ms                                                       | 442 ms: 1.05x faster                                                        |
| sympy_expand            | 599 ms                                                       | 573 ms: 1.05x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 13.6 ms: 1.04x faster                                                       |
| sympy_str               | 358 ms                                                       | 343 ms: 1.04x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.91 sec: 1.04x faster                                                      |
| telco                   | 7.14 ms                                                      | 6.90 ms: 1.04x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 757 ms: 1.03x faster                                                        |
| meteor_contest          | 137 ms                                                       | 133 ms: 1.03x faster                                                        |
| coroutines              | 30.4 ms                                                      | 30.1 ms: 1.01x faster                                                       |
| regex_dna               | 259 ms                                                       | 257 ms: 1.01x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 26.4 ms: 1.01x faster                                                       |
| pickle                  | 9.94 us                                                      | 9.96 us: 1.00x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.55 ms: 1.03x slower                                                       |
| unpickle_list           | 4.49 us                                                      | 4.68 us: 1.04x slower                                                       |
| pickle_list             | 4.11 us                                                      | 4.28 us: 1.04x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 32.2 us: 1.07x slower                                                       |
| comprehensions          | 26.9 us                                                      | 29.6 us: 1.10x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.49 ms: 1.17x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 4.03 ms: 1.17x slower                                                       |
| coverage                | 64.0 ms                                                      | 84.1 ms: 1.31x slower                                                       |
| unpack_sequence         | 59.5 ns                                                      | 152 ns: 2.55x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.14x faster                                                                |
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x
