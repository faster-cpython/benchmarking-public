
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3eb12df
- commit date: 2023-02-11
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| chameleon      | 9.17 ms                                                | 6.58 ms: 1.39x faster                                  |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| tornado_http   | 128 ms                                                 | 94.5 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| float          | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 214 ms                                                 | 199 ms: 1.07x faster                                   |
| regex_effbot   | 3.19 ms                                                | 3.56 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 288 us: 1.57x faster                                   |
| unpickle_pure_python | 302 us                                                 | 196 us: 1.54x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.2 ms: 1.35x faster                                  |
| json_loads           | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| pickle_list          | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 80.5 ms: 1.17x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| pickle               | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| pickle_dict          | 27.6 us                                                | 30.8 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.92 ms: 1.58x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.47 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| mako            | 14.7 ms                                                | 9.95 ms: 1.47x faster                                  |
| django_template | 46.3 ms                                                | 33.3 ms: 1.39x faster                                  |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230211-linux-x86_64-python-main-3.12.0a5+-3eb12df |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.11 ms: 2.34x faster                                  |
| logging_silent          | 176 ns                                                 | 91.0 ns: 1.94x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.83x faster                                   |
| richards                | 75.2 ms                                                | 42.3 ms: 1.78x faster                                  |
| pyflate                 | 676 ms                                                 | 398 ms: 1.70x faster                                   |
| go                      | 226 ms                                                 | 133 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 281 ms: 1.66x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 65.8 ms: 1.65x faster                                  |
| hexiom                  | 9.43 ms                                                | 5.91 ms: 1.59x faster                                  |
| chaos                   | 106 ms                                                 | 66.5 ms: 1.59x faster                                  |
| python_startup          | 14.1 ms                                                | 8.92 ms: 1.58x faster                                  |
| pickle_pure_python      | 452 us                                                 | 288 us: 1.57x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 75.6 ms: 1.54x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 196 us: 1.54x faster                                   |
| spectral_norm           | 150 ms                                                 | 98.5 ms: 1.52x faster                                  |
| nbody                   | 144 ms                                                 | 94.8 ms: 1.52x faster                                  |
| float                   | 109 ms                                                 | 72.1 ms: 1.51x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.3 us: 1.50x faster                                  |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                  |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                   |
| mako                    | 14.7 ms                                                | 9.95 ms: 1.47x faster                                  |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.51 ms: 1.41x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                 |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.41x faster                                  |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                 |
| pprint_safe_repr        | 953 ms                                                 | 684 ms: 1.39x faster                                   |
| django_template         | 46.3 ms                                                | 33.3 ms: 1.39x faster                                  |
| chameleon               | 9.17 ms                                                | 6.58 ms: 1.39x faster                                  |
| logging_simple          | 8.10 us                                                | 5.87 us: 1.38x faster                                  |
| async_tree_memoization  | 855 ms                                                 | 620 ms: 1.38x faster                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                   |
| logging_format          | 8.85 us                                                | 6.43 us: 1.38x faster                                  |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                  |
| async_tree_none         | 711 ms                                                 | 522 ms: 1.36x faster                                   |
| thrift                  | 1.03 ms                                                | 761 us: 1.36x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                 |
| tornado_http            | 128 ms                                                 | 94.5 ms: 1.36x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 43.9 ns: 1.35x faster                                  |
| scimark_fft             | 421 ms                                                 | 312 ms: 1.35x faster                                   |
| xml_etree_process       | 74.5 ms                                                | 55.2 ms: 1.35x faster                                  |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                   |
| 2to3                    | 335 ms                                                 | 250 ms: 1.34x faster                                   |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.13 ms: 1.32x faster                                  |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.32x faster                                  |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                   |
| nqueens                 | 100 ms                                                 | 77.6 ms: 1.29x faster                                  |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 50.8 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.27x faster                                  |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                 |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                   |
| coroutines              | 31.6 ms                                                | 25.2 ms: 1.25x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                   |
| dulwich_log             | 75.8 ms                                                | 63.1 ms: 1.20x faster                                  |
| json_loads              | 28.7 us                                                | 24.0 us: 1.20x faster                                  |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.19x faster                                  |
| sympy_str               | 325 ms                                                 | 273 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| pickle_list             | 4.72 us                                                | 4.05 us: 1.17x faster                                  |
| xml_etree_generate      | 93.8 ms                                                | 80.5 ms: 1.17x faster                                  |
| sympy_expand            | 534 ms                                                 | 459 ms: 1.16x faster                                   |
| json                    | 5.35 ms                                                | 4.63 ms: 1.16x faster                                  |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| djangocms               | 36.9 us                                                | 32.2 us: 1.15x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.45 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                  |
| mdp                     | 2.74 sec                                               | 2.47 sec: 1.11x faster                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 214 ms                                                 | 199 ms: 1.07x faster                                   |
| telco                   | 6.73 ms                                                | 6.34 ms: 1.06x faster                                  |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                  |
| pickle                  | 10.2 us                                                | 10.1 us: 1.01x faster                                  |
| async_generators        | 426 ms                                                 | 428 ms: 1.00x slower                                   |
| generators              | 76.4 ms                                                | 77.5 ms: 1.01x slower                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.56 ms: 1.11x slower                                  |
| pickle_dict             | 27.6 us                                                | 30.8 us: 1.12x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.47 ms: 1.12x slower                                  |
| gc_traversal            | 3.53 ms                                                | 4.16 ms: 1.18x slower                                  |
| coverage                | 74.7 ms                                                | 96.8 ms: 1.30x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
