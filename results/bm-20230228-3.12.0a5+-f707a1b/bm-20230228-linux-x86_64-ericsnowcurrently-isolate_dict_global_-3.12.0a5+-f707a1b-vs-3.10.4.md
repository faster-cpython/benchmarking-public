
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_dict_global_
- machine: linux-x86_64
- commit hash: f707a1b
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 251 ms: 1.33x faster                                                              |
| chameleon      | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                             |
| docutils       | 3.18 sec                                               | 2.57 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                             |
| tornado_http   | 128 ms                                                 | 95.5 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.9 ms: 1.53x faster                                                             |
| float          | 109 ms                                                 | 74.3 ms: 1.47x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                              |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.61x faster                                                              |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                              |
| json_dumps           | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                             |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                             |
| json_loads           | 28.7 us                                                | 24.3 us: 1.18x faster                                                             |
| xml_etree_generate   | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                             |
| pickle_list          | 4.72 us                                                | 4.09 us: 1.15x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.06x faster                                                              |
| unpickle             | 14.2 us                                                | 13.6 us: 1.04x faster                                                             |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                             |
| unpickle_list        | 4.92 us                                                | 4.96 us: 1.01x slower                                                             |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.11x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.06 ms: 1.56x faster                                                             |
| python_startup_no_site | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.81 ms: 1.49x faster                                                             |
| genshi_text     | 30.6 ms                                                | 21.4 ms: 1.43x faster                                                             |
| django_template | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                             |
| genshi_xml      | 63.7 ms                                                | 48.6 ms: 1.31x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.6 ms: 2.50x faster                                                             |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                                             |
| logging_silent          | 176 ns                                                 | 94.5 ns: 1.87x faster                                                             |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                              |
| asyncio_tcp             | 914 ms                                                 | 503 ms: 1.82x faster                                                              |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                                             |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                              |
| scimark_monte_carlo     | 109 ms                                                 | 66.6 ms: 1.63x faster                                                             |
| pyflate                 | 676 ms                                                 | 417 ms: 1.62x faster                                                              |
| raytrace                | 467 ms                                                 | 289 ms: 1.62x faster                                                              |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.61x faster                                                              |
| spectral_norm           | 150 ms                                                 | 93.8 ms: 1.59x faster                                                             |
| crypto_pyaes            | 117 ms                                                 | 73.6 ms: 1.59x faster                                                             |
| python_startup          | 14.1 ms                                                | 9.06 ms: 1.56x faster                                                             |
| chaos                   | 106 ms                                                 | 68.5 ms: 1.54x faster                                                             |
| nbody                   | 144 ms                                                 | 93.9 ms: 1.53x faster                                                             |
| hexiom                  | 9.43 ms                                                | 6.16 ms: 1.53x faster                                                             |
| deepcopy_memo           | 51.7 us                                                | 34.1 us: 1.52x faster                                                             |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                              |
| mako                    | 14.7 ms                                                | 9.81 ms: 1.49x faster                                                             |
| float                   | 109 ms                                                 | 74.3 ms: 1.47x faster                                                             |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                              |
| chameleon               | 9.17 ms                                                | 6.28 ms: 1.46x faster                                                             |
| genshi_text             | 30.6 ms                                                | 21.4 ms: 1.43x faster                                                             |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                            |
| logging_format          | 8.85 us                                                | 6.27 us: 1.41x faster                                                             |
| json_dumps              | 13.4 ms                                                | 9.55 ms: 1.41x faster                                                             |
| pprint_safe_repr        | 953 ms                                                 | 679 ms: 1.40x faster                                                              |
| django_template         | 46.3 ms                                                | 33.0 ms: 1.40x faster                                                             |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                                             |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.75 ms: 1.39x faster                                                             |
| async_tree_io           | 1.78 sec                                               | 1.28 sec: 1.39x faster                                                            |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                                            |
| async_tree_none         | 711 ms                                                 | 523 ms: 1.36x faster                                                              |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                                              |
| fannkuch                | 488 ms                                                 | 362 ms: 1.35x faster                                                              |
| coroutines              | 31.6 ms                                                | 23.5 ms: 1.35x faster                                                             |
| tornado_http            | 128 ms                                                 | 95.5 ms: 1.34x faster                                                             |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                             |
| unpack_sequence         | 59.4 ns                                                | 44.3 ns: 1.34x faster                                                             |
| 2to3                    | 335 ms                                                 | 251 ms: 1.33x faster                                                              |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                              |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                             |
| deepcopy                | 438 us                                                 | 331 us: 1.32x faster                                                              |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.32x faster                                                             |
| async_tree_memoization  | 855 ms                                                 | 650 ms: 1.32x faster                                                              |
| genshi_xml              | 63.7 ms                                                | 48.6 ms: 1.31x faster                                                             |
| thrift                  | 1.03 ms                                                | 793 us: 1.30x faster                                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 737 ms: 1.29x faster                                                              |
| mypy2                   | 430 ms                                                 | 334 ms: 1.29x faster                                                              |
| deepcopy_reduce         | 3.79 us                                                | 2.95 us: 1.28x faster                                                             |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                              |
| sqlglot_optimize        | 65.2 ms                                                | 51.6 ms: 1.26x faster                                                             |
| nqueens                 | 100 ms                                                 | 80.5 ms: 1.24x faster                                                             |
| docutils                | 3.18 sec                                               | 2.57 sec: 1.24x faster                                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.42 ms: 1.23x faster                                                             |
| dulwich_log             | 75.8 ms                                                | 63.8 ms: 1.19x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                              |
| bench_thread_pool       | 946 us                                                 | 797 us: 1.19x faster                                                              |
| json_loads              | 28.7 us                                                | 24.3 us: 1.18x faster                                                             |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.2 ms: 1.18x faster                                                             |
| xml_etree_generate      | 93.8 ms                                                | 80.8 ms: 1.16x faster                                                             |
| sympy_integrate         | 24.0 ms                                                | 20.8 ms: 1.16x faster                                                             |
| json                    | 5.35 ms                                                | 4.62 ms: 1.16x faster                                                             |
| pickle_list             | 4.72 us                                                | 4.09 us: 1.15x faster                                                             |
| sympy_expand            | 534 ms                                                 | 466 ms: 1.15x faster                                                              |
| mdp                     | 2.74 sec                                               | 2.40 sec: 1.14x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                                             |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                             |
| sympy_str               | 325 ms                                                 | 289 ms: 1.12x faster                                                              |
| sqlite_synth            | 2.92 us                                                | 2.63 us: 1.11x faster                                                             |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                                             |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                              |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.06x faster                                                              |
| telco                   | 6.73 ms                                                | 6.40 ms: 1.05x faster                                                             |
| unpickle                | 14.2 us                                                | 13.6 us: 1.04x faster                                                             |
| async_generators        | 426 ms                                                 | 417 ms: 1.02x faster                                                              |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                             |
| unpickle_list           | 4.92 us                                                | 4.96 us: 1.01x slower                                                             |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                                             |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.11x slower                                                             |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                                             |
| python_startup_no_site  | 5.78 ms                                                | 6.57 ms: 1.14x slower                                                             |
| dask                    | 436 ms                                                 | 510 ms: 1.17x slower                                                              |
| coverage                | 74.7 ms                                                | 93.1 ms: 1.25x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230228-3.12.0a5+-f707a1b/bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b.json: comprehensions
