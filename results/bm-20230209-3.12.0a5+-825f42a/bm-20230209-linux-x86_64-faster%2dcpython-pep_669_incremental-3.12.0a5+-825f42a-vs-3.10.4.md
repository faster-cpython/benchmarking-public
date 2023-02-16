
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 825f42a
- commit date: 2023-02-09
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 246 ms: 1.37x faster                                                            |
| chameleon      | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                           |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                          |
| html5lib       | 85.9 ms                                                | 58.7 ms: 1.46x faster                                                           |
| tornado_http   | 128 ms                                                 | 92.8 ms: 1.38x faster                                                           |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 90.7 ms: 1.59x faster                                                           |
| float          | 109 ms                                                 | 71.4 ms: 1.53x faster                                                           |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 124 ms: 1.43x faster                                                            |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                           |
| regex_dna      | 214 ms                                                 | 201 ms: 1.06x faster                                                            |
| regex_effbot   | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 279 us: 1.62x faster                                                            |
| unpickle_pure_python | 302 us                                                 | 194 us: 1.55x faster                                                            |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.42x faster                                                           |
| xml_etree_process    | 74.5 ms                                                | 55.1 ms: 1.35x faster                                                           |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                                           |
| xml_etree_generate   | 93.8 ms                                                | 79.6 ms: 1.18x faster                                                           |
| pickle_list          | 4.72 us                                                | 4.04 us: 1.17x faster                                                           |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.10x faster                                                            |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| unpickle             | 14.2 us                                                | 13.5 us: 1.05x faster                                                           |
| pickle               | 10.2 us                                                | 10.0 us: 1.01x faster                                                           |
| unpickle_list        | 4.92 us                                                | 5.15 us: 1.05x slower                                                           |
| pickle_dict          | 27.6 us                                                | 29.4 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.94 ms: 1.57x faster                                                           |
| python_startup_no_site | 5.78 ms                                                | 6.50 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                           |
| mako            | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                           |
| django_template | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                           |
| genshi_xml      | 63.7 ms                                                | 45.5 ms: 1.40x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.11 ms: 2.34x faster                                                           |
| scimark_sor             | 197 ms                                                 | 102 ms: 1.93x faster                                                            |
| logging_silent          | 176 ns                                                 | 93.1 ns: 1.90x faster                                                           |
| richards                | 75.2 ms                                                | 41.2 ms: 1.82x faster                                                           |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                                            |
| go                      | 226 ms                                                 | 129 ms: 1.75x faster                                                            |
| scimark_monte_carlo     | 109 ms                                                 | 63.8 ms: 1.70x faster                                                           |
| raytrace                | 467 ms                                                 | 276 ms: 1.69x faster                                                            |
| chaos                   | 106 ms                                                 | 62.6 ms: 1.69x faster                                                           |
| pyflate                 | 676 ms                                                 | 410 ms: 1.65x faster                                                            |
| hexiom                  | 9.43 ms                                                | 5.79 ms: 1.63x faster                                                           |
| pickle_pure_python      | 452 us                                                 | 279 us: 1.62x faster                                                            |
| crypto_pyaes            | 117 ms                                                 | 72.1 ms: 1.62x faster                                                           |
| spectral_norm           | 150 ms                                                 | 93.3 ms: 1.60x faster                                                           |
| nbody                   | 144 ms                                                 | 90.7 ms: 1.59x faster                                                           |
| python_startup          | 14.1 ms                                                | 8.94 ms: 1.57x faster                                                           |
| scimark_lu              | 161 ms                                                 | 103 ms: 1.57x faster                                                            |
| unpickle_pure_python    | 302 us                                                 | 194 us: 1.55x faster                                                            |
| deepcopy_memo           | 51.7 us                                                | 33.3 us: 1.55x faster                                                           |
| float                   | 109 ms                                                 | 71.4 ms: 1.53x faster                                                           |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.50x faster                                                           |
| mako                    | 14.7 ms                                                | 9.79 ms: 1.50x faster                                                           |
| chameleon               | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                           |
| html5lib                | 85.9 ms                                                | 58.7 ms: 1.46x faster                                                           |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                           |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                          |
| django_template         | 46.3 ms                                                | 32.2 ms: 1.44x faster                                                           |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                           |
| logging_simple          | 8.10 us                                                | 5.65 us: 1.43x faster                                                           |
| regex_compile           | 177 ms                                                 | 124 ms: 1.43x faster                                                            |
| pprint_safe_repr        | 953 ms                                                 | 668 ms: 1.43x faster                                                            |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.42x faster                                                           |
| unpack_sequence         | 59.4 ns                                                | 41.8 ns: 1.42x faster                                                           |
| pycparser               | 1.53 sec                                               | 1.08 sec: 1.42x faster                                                          |
| logging_format          | 8.85 us                                                | 6.26 us: 1.41x faster                                                           |
| scimark_fft             | 421 ms                                                 | 299 ms: 1.41x faster                                                            |
| genshi_xml              | 63.7 ms                                                | 45.5 ms: 1.40x faster                                                           |
| generators              | 76.4 ms                                                | 54.8 ms: 1.40x faster                                                           |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.92 ms: 1.39x faster                                                           |
| tornado_http            | 128 ms                                                 | 92.8 ms: 1.38x faster                                                           |
| 2to3                    | 335 ms                                                 | 246 ms: 1.37x faster                                                            |
| aiohttp                 | 1.34 ms                                                | 983 us: 1.36x faster                                                            |
| deepcopy                | 438 us                                                 | 321 us: 1.36x faster                                                            |
| thrift                  | 1.03 ms                                                | 762 us: 1.36x faster                                                            |
| gunicorn                | 1.43 ms                                                | 1.05 ms: 1.36x faster                                                           |
| xml_etree_process       | 74.5 ms                                                | 55.1 ms: 1.35x faster                                                           |
| fannkuch                | 488 ms                                                 | 361 ms: 1.35x faster                                                            |
| async_tree_none         | 711 ms                                                 | 529 ms: 1.34x faster                                                            |
| mypy2                   | 430 ms                                                 | 322 ms: 1.34x faster                                                            |
| async_tree_memoization  | 855 ms                                                 | 643 ms: 1.33x faster                                                            |
| async_tree_io           | 1.78 sec                                               | 1.34 sec: 1.33x faster                                                          |
| deepcopy_reduce         | 3.79 us                                                | 2.86 us: 1.33x faster                                                           |
| nqueens                 | 100 ms                                                 | 75.5 ms: 1.33x faster                                                           |
| sqlglot_normalize       | 134 ms                                                 | 102 ms: 1.32x faster                                                            |
| sqlglot_optimize        | 65.2 ms                                                | 49.8 ms: 1.31x faster                                                           |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                          |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.3 ms: 1.24x faster                                                           |
| async_tree_cpu_io_mixed | 949 ms                                                 | 767 ms: 1.24x faster                                                            |
| sympy_integrate         | 24.0 ms                                                | 19.5 ms: 1.23x faster                                                           |
| sqlalchemy_declarative  | 165 ms                                                 | 134 ms: 1.23x faster                                                            |
| dulwich_log             | 75.8 ms                                                | 61.5 ms: 1.23x faster                                                           |
| bench_thread_pool       | 946 us                                                 | 771 us: 1.23x faster                                                            |
| sympy_str               | 325 ms                                                 | 265 ms: 1.22x faster                                                            |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                                           |
| sympy_expand            | 534 ms                                                 | 446 ms: 1.20x faster                                                            |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.19x faster                                                            |
| xml_etree_generate      | 93.8 ms                                                | 79.6 ms: 1.18x faster                                                           |
| json                    | 5.35 ms                                                | 4.56 ms: 1.17x faster                                                           |
| pickle_list             | 4.72 us                                                | 4.04 us: 1.17x faster                                                           |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                           |
| djangocms               | 36.9 us                                                | 32.1 us: 1.15x faster                                                           |
| sqlite_synth            | 2.92 us                                                | 2.58 us: 1.13x faster                                                           |
| create_gc_cycles        | 1.65 ms                                                | 1.47 ms: 1.12x faster                                                           |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                           |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.10x faster                                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                            |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                            |
| regex_dna               | 214 ms                                                 | 201 ms: 1.06x faster                                                            |
| telco                   | 6.73 ms                                                | 6.35 ms: 1.06x faster                                                           |
| unpickle                | 14.2 us                                                | 13.5 us: 1.05x faster                                                           |
| mdp                     | 2.74 sec                                               | 2.67 sec: 1.03x faster                                                          |
| async_generators        | 426 ms                                                 | 420 ms: 1.02x faster                                                            |
| pickle                  | 10.2 us                                                | 10.0 us: 1.01x faster                                                           |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                            |
| unpickle_list           | 4.92 us                                                | 5.15 us: 1.05x slower                                                           |
| pickle_dict             | 27.6 us                                                | 29.4 us: 1.06x slower                                                           |
| gc_traversal            | 3.53 ms                                                | 3.80 ms: 1.08x slower                                                           |
| regex_effbot            | 3.19 ms                                                | 3.57 ms: 1.12x slower                                                           |
| python_startup_no_site  | 5.78 ms                                                | 6.50 ms: 1.13x slower                                                           |
| coverage                | 74.7 ms                                                | 97.7 ms: 1.31x slower                                                           |
| coroutines              | 31.6 ms                                                | 54.8 ms: 1.73x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, flaskblogging, pylint
