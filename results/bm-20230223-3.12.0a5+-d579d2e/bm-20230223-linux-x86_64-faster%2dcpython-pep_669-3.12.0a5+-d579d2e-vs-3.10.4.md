
# Results vs. 3.10.4

- fork: faster-cpython
- ref: pep_669
- machine: linux-x86_64
- commit hash: d579d2e
- commit date: 2023-02-23
- overall geometric mean: 1.31x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 247 ms: 1.36x faster                                                |
| chameleon      | 9.17 ms                                                | 6.26 ms: 1.46x faster                                               |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.26x faster                                              |
| html5lib       | 85.9 ms                                                | 59.8 ms: 1.44x faster                                               |
| tornado_http   | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.38x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.2 ms: 1.56x faster                                               |
| float          | 109 ms                                                 | 73.4 ms: 1.48x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.32x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 200 ms: 1.07x faster                                                |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 277 us: 1.63x faster                                                |
| unpickle_pure_python | 302 us                                                 | 194 us: 1.55x faster                                                |
| json_dumps           | 13.4 ms                                                | 9.40 ms: 1.43x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 54.4 ms: 1.37x faster                                               |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                               |
| xml_etree_generate   | 93.8 ms                                                | 79.4 ms: 1.18x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.11x faster                                               |
| pickle_list          | 4.72 us                                                | 4.27 us: 1.10x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| unpickle_list        | 4.92 us                                                | 4.98 us: 1.01x slower                                               |
| pickle_dict          | 27.6 us                                                | 31.7 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.06 ms: 1.55x faster                                               |
| python_startup_no_site | 5.78 ms                                                | 6.58 ms: 1.14x slower                                               |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.75 ms: 1.50x faster                                               |
| genshi_text     | 30.6 ms                                                | 20.5 ms: 1.50x faster                                               |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                               |
| genshi_xml      | 63.7 ms                                                | 45.9 ms: 1.39x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230223-linux-x86_64-faster%2dcpython-pep_669-3.12.0a5+-d579d2e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 31.6 ms: 2.42x faster                                               |
| deltablue               | 7.28 ms                                                | 3.14 ms: 2.32x faster                                               |
| logging_silent          | 176 ns                                                 | 91.7 ns: 1.92x faster                                               |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.90x faster                                                |
| asyncio_tcp             | 914 ms                                                 | 498 ms: 1.83x faster                                                |
| richards                | 75.2 ms                                                | 41.6 ms: 1.81x faster                                               |
| go                      | 226 ms                                                 | 130 ms: 1.73x faster                                                |
| scimark_monte_carlo     | 109 ms                                                 | 64.2 ms: 1.69x faster                                               |
| pyflate                 | 676 ms                                                 | 401 ms: 1.69x faster                                                |
| raytrace                | 467 ms                                                 | 280 ms: 1.67x faster                                                |
| pickle_pure_python      | 452 us                                                 | 277 us: 1.63x faster                                                |
| crypto_pyaes            | 117 ms                                                 | 72.4 ms: 1.61x faster                                               |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.59x faster                                               |
| spectral_norm           | 150 ms                                                 | 94.6 ms: 1.58x faster                                               |
| hexiom                  | 9.43 ms                                                | 6.00 ms: 1.57x faster                                               |
| deepcopy_memo           | 51.7 us                                                | 33.1 us: 1.56x faster                                               |
| nbody                   | 144 ms                                                 | 92.2 ms: 1.56x faster                                               |
| python_startup          | 14.1 ms                                                | 9.06 ms: 1.55x faster                                               |
| unpickle_pure_python    | 302 us                                                 | 194 us: 1.55x faster                                                |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                |
| mako                    | 14.7 ms                                                | 9.75 ms: 1.50x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.5 ms: 1.50x faster                                               |
| float                   | 109 ms                                                 | 73.4 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.39 ms: 1.47x faster                                               |
| chameleon               | 9.17 ms                                                | 6.26 ms: 1.46x faster                                               |
| pprint_pformat          | 1.98 sec                                               | 1.37 sec: 1.45x faster                                              |
| sqlglot_transpile       | 2.43 ms                                                | 1.68 ms: 1.44x faster                                               |
| pprint_safe_repr        | 953 ms                                                 | 662 ms: 1.44x faster                                                |
| coroutines              | 31.6 ms                                                | 22.0 ms: 1.44x faster                                               |
| html5lib                | 85.9 ms                                                | 59.8 ms: 1.44x faster                                               |
| json_dumps              | 13.4 ms                                                | 9.40 ms: 1.43x faster                                               |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                               |
| logging_simple          | 8.10 us                                                | 5.78 us: 1.40x faster                                               |
| pycparser               | 1.53 sec                                               | 1.09 sec: 1.40x faster                                              |
| scimark_fft             | 421 ms                                                 | 302 ms: 1.39x faster                                                |
| genshi_xml              | 63.7 ms                                                | 45.9 ms: 1.39x faster                                               |
| regex_compile           | 177 ms                                                 | 129 ms: 1.38x faster                                                |
| unpack_sequence         | 59.4 ns                                                | 43.1 ns: 1.38x faster                                               |
| logging_format          | 8.85 us                                                | 6.46 us: 1.37x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 54.4 ms: 1.37x faster                                               |
| thrift                  | 1.03 ms                                                | 756 us: 1.37x faster                                                |
| fannkuch                | 488 ms                                                 | 357 ms: 1.37x faster                                                |
| tornado_http            | 128 ms                                                 | 93.8 ms: 1.37x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                              |
| 2to3                    | 335 ms                                                 | 247 ms: 1.36x faster                                                |
| deepcopy                | 438 us                                                 | 323 us: 1.36x faster                                                |
| async_tree_none         | 711 ms                                                 | 526 ms: 1.35x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| async_tree_memoization  | 855 ms                                                 | 646 ms: 1.32x faster                                                |
| sqlglot_normalize       | 134 ms                                                 | 102 ms: 1.32x faster                                                |
| mypy2                   | 430 ms                                                 | 327 ms: 1.31x faster                                                |
| sqlglot_optimize        | 65.2 ms                                                | 50.1 ms: 1.30x faster                                               |
| deepcopy_reduce         | 3.79 us                                                | 2.92 us: 1.30x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 741 ms: 1.28x faster                                                |
| nqueens                 | 100 ms                                                 | 78.4 ms: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.26x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.34 ms: 1.26x faster                                               |
| dulwich_log             | 75.8 ms                                                | 61.6 ms: 1.23x faster                                               |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.6 ms: 1.22x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                |
| bench_thread_pool       | 946 us                                                 | 782 us: 1.21x faster                                                |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                               |
| sympy_integrate         | 24.0 ms                                                | 20.2 ms: 1.19x faster                                               |
| sympy_expand            | 534 ms                                                 | 451 ms: 1.18x faster                                                |
| xml_etree_generate      | 93.8 ms                                                | 79.4 ms: 1.18x faster                                               |
| json                    | 5.35 ms                                                | 4.58 ms: 1.17x faster                                               |
| sympy_str               | 325 ms                                                 | 279 ms: 1.16x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                               |
| djangocms               | 36.9 us                                                | 32.3 us: 1.14x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.6 ms: 1.13x faster                                               |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.12x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.11x faster                                               |
| sympy_sum               | 183 ms                                                 | 165 ms: 1.11x faster                                                |
| pickle_list             | 4.72 us                                                | 4.27 us: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| create_gc_cycles        | 1.65 ms                                                | 1.51 ms: 1.09x faster                                               |
| sqlite_synth            | 2.92 us                                                | 2.73 us: 1.07x faster                                               |
| regex_dna               | 214 ms                                                 | 200 ms: 1.07x faster                                                |
| telco                   | 6.73 ms                                                | 6.35 ms: 1.06x faster                                               |
| mdp                     | 2.74 sec                                               | 2.60 sec: 1.05x faster                                              |
| async_generators        | 426 ms                                                 | 430 ms: 1.01x slower                                                |
| unpickle_list           | 4.92 us                                                | 4.98 us: 1.01x slower                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                               |
| dask                    | 436 ms                                                 | 490 ms: 1.12x slower                                                |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                               |
| python_startup_no_site  | 5.78 ms                                                | 6.58 ms: 1.14x slower                                               |
| pickle_dict             | 27.6 us                                                | 31.7 us: 1.15x slower                                               |
| coverage                | 74.7 ms                                                | 96.9 ms: 1.30x slower                                               |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                        |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
