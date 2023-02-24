
# Results vs. 3.10.4

- fork: faster-cpython
- ref: backedge_counter
- machine: linux-x86_64
- commit hash: 7404033
- commit date: 2023-02-24
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 248 ms: 1.35x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                        |
| docutils       | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                       |
| html5lib       | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.1 ms: 1.55x faster                                                        |
| float          | 109 ms                                                 | 72.5 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.36x faster                                                         |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                        |
| regex_dna      | 214 ms                                                 | 213 ms: 1.00x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 289 us: 1.56x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                        |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.00 us: 1.18x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 81.2 ms: 1.16x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| unpickle             | 14.2 us                                                | 13.2 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| pickle               | 10.2 us                                                | 10.2 us: 1.01x slower                                                        |
| unpickle_list        | 4.92 us                                                | 5.10 us: 1.04x slower                                                        |
| pickle_dict          | 27.6 us                                                | 30.3 us: 1.10x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                        |
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                        |
| django_template | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230224-linux-x86_64-faster%2dcpython-backedge_counter-3.12.0a5+-7404033 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.0 ms: 2.55x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.15 ms: 2.31x faster                                                        |
| logging_silent          | 176 ns                                                 | 93.2 ns: 1.89x faster                                                        |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                         |
| asyncio_tcp             | 914 ms                                                 | 506 ms: 1.81x faster                                                         |
| richards                | 75.2 ms                                                | 43.2 ms: 1.74x faster                                                        |
| pyflate                 | 676 ms                                                 | 397 ms: 1.70x faster                                                         |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                         |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                 | 65.4 ms: 1.66x faster                                                        |
| spectral_norm           | 150 ms                                                 | 92.4 ms: 1.62x faster                                                        |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.59x faster                                                        |
| hexiom                  | 9.43 ms                                                | 5.98 ms: 1.58x faster                                                        |
| crypto_pyaes            | 117 ms                                                 | 74.5 ms: 1.57x faster                                                        |
| python_startup          | 14.1 ms                                                | 9.00 ms: 1.56x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 289 us: 1.56x faster                                                         |
| nbody                   | 144 ms                                                 | 93.1 ms: 1.55x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                                         |
| float                   | 109 ms                                                 | 72.5 ms: 1.50x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                | 9.93 ms: 1.48x faster                                                        |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.47x faster                                                        |
| scimark_lu              | 161 ms                                                 | 110 ms: 1.46x faster                                                         |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 667 ms: 1.43x faster                                                         |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.47 ms: 1.42x faster                                                        |
| coroutines              | 31.6 ms                                                | 22.3 ms: 1.42x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.48 ms: 1.41x faster                                                        |
| html5lib                | 85.9 ms                                                | 61.0 ms: 1.41x faster                                                        |
| django_template         | 46.3 ms                                                | 32.9 ms: 1.41x faster                                                        |
| logging_format          | 8.85 us                                                | 6.31 us: 1.40x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                                        |
| pycparser               | 1.53 sec                                               | 1.10 sec: 1.39x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 43.5 ns: 1.37x faster                                                        |
| async_tree_none         | 711 ms                                                 | 521 ms: 1.36x faster                                                         |
| genshi_xml              | 63.7 ms                                                | 47.0 ms: 1.36x faster                                                        |
| regex_compile           | 177 ms                                                 | 131 ms: 1.36x faster                                                         |
| 2to3                    | 335 ms                                                 | 248 ms: 1.35x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| thrift                  | 1.03 ms                                                | 769 us: 1.34x faster                                                         |
| scimark_fft             | 421 ms                                                 | 313 ms: 1.34x faster                                                         |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                                        |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                                         |
| deepcopy                | 438 us                                                 | 329 us: 1.33x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 654 ms: 1.31x faster                                                         |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.30x faster                                                         |
| mypy2                   | 430 ms                                                 | 332 ms: 1.30x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.1 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                         |
| deepcopy_reduce         | 3.79 us                                                | 2.99 us: 1.27x faster                                                        |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                        |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.21x faster                                                         |
| dulwich_log             | 75.8 ms                                                | 62.8 ms: 1.21x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 786 us: 1.20x faster                                                         |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| docutils                | 3.18 sec                                               | 2.65 sec: 1.20x faster                                                       |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.00 us: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                                        |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.68 ms: 1.16x faster                                                        |
| djangocms               | 36.9 us                                                | 31.7 us: 1.16x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 81.2 ms: 1.16x faster                                                        |
| sympy_str               | 325 ms                                                 | 283 ms: 1.15x faster                                                         |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                        |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                                         |
| sqlite_synth            | 2.92 us                                                | 2.64 us: 1.11x faster                                                        |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.10x faster                                                         |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| mdp                     | 2.74 sec                                               | 2.52 sec: 1.09x faster                                                       |
| unpickle                | 14.2 us                                                | 13.2 us: 1.07x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| telco                   | 6.73 ms                                                | 6.43 ms: 1.05x faster                                                        |
| async_generators        | 426 ms                                                 | 422 ms: 1.01x faster                                                         |
| regex_dna               | 214 ms                                                 | 213 ms: 1.00x faster                                                         |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                         |
| pickle                  | 10.2 us                                                | 10.2 us: 1.01x slower                                                        |
| regex_effbot            | 3.19 ms                                                | 3.27 ms: 1.02x slower                                                        |
| unpickle_list           | 4.92 us                                                | 5.10 us: 1.04x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.3 us: 1.10x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.55 ms: 1.13x slower                                                        |
| dask                    | 436 ms                                                 | 499 ms: 1.14x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 4.07 ms: 1.15x slower                                                        |
| coverage                | 74.7 ms                                                | 97.1 ms: 1.30x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
