
# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_deep_freeze
- machine: linux-x86_64
- commit hash: 76326f3
- commit date: 2023-03-16
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| chameleon      | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                      |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                     |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                                      |
| tornado_http   | 128 ms                                                 | 90.9 ms: 1.41x faster                                                      |
| Geometric mean | (ref)                                                  | 1.38x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 88.2 ms: 1.63x faster                                                      |
| float          | 109 ms                                                 | 73.7 ms: 1.48x faster                                                      |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.34x faster                                                       |
| regex_dna      | 214 ms                                                 | 204 ms: 1.05x faster                                                       |
| regex_v8       | 25.0 ms                                                | 25.6 ms: 1.02x slower                                                      |
| regex_effbot   | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 282 us: 1.60x faster                                                       |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.52x faster                                                       |
| json_dumps           | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                      |
| xml_etree_process    | 74.5 ms                                                | 56.4 ms: 1.32x faster                                                      |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| xml_etree_generate   | 93.8 ms                                                | 81.8 ms: 1.15x faster                                                      |
| pickle_list          | 4.72 us                                                | 4.21 us: 1.12x faster                                                      |
| xml_etree_iterparse  | 111 ms                                                 | 99.7 ms: 1.11x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.11x faster                                                       |
| unpickle_list        | 4.92 us                                                | 5.32 us: 1.08x slower                                                      |
| pickle_dict          | 27.6 us                                                | 30.0 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmark hidden because not significant (2): pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.51 ms: 1.48x faster                                                      |
| python_startup_no_site | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| mako            | 14.7 ms                                                | 10.2 ms: 1.44x faster                                                      |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                      |
| genshi_xml      | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 29.9 ms: 2.55x faster                                                      |
| deltablue               | 7.28 ms                                                | 3.15 ms: 2.31x faster                                                      |
| logging_silent          | 176 ns                                                 | 93.4 ns: 1.89x faster                                                      |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.86x faster                                                       |
| asyncio_tcp             | 914 ms                                                 | 507 ms: 1.80x faster                                                       |
| richards                | 75.2 ms                                                | 42.6 ms: 1.76x faster                                                      |
| go                      | 226 ms                                                 | 132 ms: 1.71x faster                                                       |
| raytrace                | 467 ms                                                 | 282 ms: 1.66x faster                                                       |
| spectral_norm           | 150 ms                                                 | 90.6 ms: 1.65x faster                                                      |
| nbody                   | 144 ms                                                 | 88.2 ms: 1.63x faster                                                      |
| scimark_monte_carlo     | 109 ms                                                 | 67.0 ms: 1.62x faster                                                      |
| pickle_pure_python      | 452 us                                                 | 282 us: 1.60x faster                                                       |
| pyflate                 | 676 ms                                                 | 423 ms: 1.60x faster                                                       |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.58x faster                                                      |
| crypto_pyaes            | 117 ms                                                 | 74.4 ms: 1.57x faster                                                      |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                      |
| deepcopy_memo           | 51.7 us                                                | 33.7 us: 1.53x faster                                                      |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.52x faster                                                       |
| scimark_lu              | 161 ms                                                 | 106 ms: 1.51x faster                                                       |
| python_startup          | 14.1 ms                                                | 9.51 ms: 1.48x faster                                                      |
| float                   | 109 ms                                                 | 73.7 ms: 1.48x faster                                                      |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                                      |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                                      |
| chameleon               | 9.17 ms                                                | 6.36 ms: 1.44x faster                                                      |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.44x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.42 ms: 1.44x faster                                                      |
| coroutines              | 31.6 ms                                                | 22.2 ms: 1.42x faster                                                      |
| logging_simple          | 8.10 us                                                | 5.69 us: 1.42x faster                                                      |
| sqlglot_transpile       | 2.43 ms                                                | 1.71 ms: 1.42x faster                                                      |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                                     |
| async_tree_memoization  | 855 ms                                                 | 606 ms: 1.41x faster                                                       |
| tornado_http            | 128 ms                                                 | 90.9 ms: 1.41x faster                                                      |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                                      |
| json_dumps              | 13.4 ms                                                | 9.62 ms: 1.40x faster                                                      |
| logging_format          | 8.85 us                                                | 6.34 us: 1.40x faster                                                      |
| pprint_safe_repr        | 953 ms                                                 | 687 ms: 1.39x faster                                                       |
| unpack_sequence         | 59.4 ns                                                | 42.8 ns: 1.39x faster                                                      |
| scimark_fft             | 421 ms                                                 | 304 ms: 1.38x faster                                                       |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.37x faster                                                     |
| aiohttp                 | 1.34 ms                                                | 996 us: 1.34x faster                                                       |
| thrift                  | 1.03 ms                                                | 772 us: 1.34x faster                                                       |
| regex_compile           | 177 ms                                                 | 133 ms: 1.34x faster                                                       |
| genshi_xml              | 63.7 ms                                                | 47.7 ms: 1.34x faster                                                      |
| deepcopy                | 438 us                                                 | 328 us: 1.33x faster                                                       |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                       |
| gunicorn                | 1.43 ms                                                | 1.07 ms: 1.33x faster                                                      |
| async_tree_none         | 711 ms                                                 | 535 ms: 1.33x faster                                                       |
| xml_etree_process       | 74.5 ms                                                | 56.4 ms: 1.32x faster                                                      |
| fannkuch                | 488 ms                                                 | 371 ms: 1.31x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.17 sec: 1.31x faster                                                     |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                       |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                                      |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                      |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                                     |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.37 ms: 1.25x faster                                                      |
| nqueens                 | 100 ms                                                 | 81.1 ms: 1.23x faster                                                      |
| async_tree_cpu_io_mixed | 949 ms                                                 | 770 ms: 1.23x faster                                                       |
| dulwich_log             | 75.8 ms                                                | 62.3 ms: 1.22x faster                                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                       |
| sqlalchemy_imperative   | 21.5 ms                                                | 17.8 ms: 1.20x faster                                                      |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                      |
| bench_thread_pool       | 946 us                                                 | 791 us: 1.20x faster                                                       |
| sympy_integrate         | 24.0 ms                                                | 20.4 ms: 1.18x faster                                                      |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                                      |
| sympy_expand            | 534 ms                                                 | 464 ms: 1.15x faster                                                       |
| xml_etree_generate      | 93.8 ms                                                | 81.8 ms: 1.15x faster                                                      |
| mdp                     | 2.74 sec                                               | 2.40 sec: 1.14x faster                                                     |
| sympy_str               | 325 ms                                                 | 284 ms: 1.14x faster                                                       |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                                      |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                      |
| pickle_list             | 4.72 us                                                | 4.21 us: 1.12x faster                                                      |
| xml_etree_iterparse     | 111 ms                                                 | 99.7 ms: 1.11x faster                                                      |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                      |
| sympy_sum               | 183 ms                                                 | 166 ms: 1.11x faster                                                       |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.11x faster                                                       |
| sqlite_synth            | 2.92 us                                                | 2.65 us: 1.10x faster                                                      |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.10x faster                                                       |
| regex_dna               | 214 ms                                                 | 204 ms: 1.05x faster                                                       |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                                       |
| telco                   | 6.73 ms                                                | 6.56 ms: 1.03x faster                                                      |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                       |
| regex_v8                | 25.0 ms                                                | 25.6 ms: 1.02x slower                                                      |
| gc_traversal            | 3.53 ms                                                | 3.68 ms: 1.04x slower                                                      |
| regex_effbot            | 3.19 ms                                                | 3.45 ms: 1.08x slower                                                      |
| unpickle_list           | 4.92 us                                                | 5.32 us: 1.08x slower                                                      |
| pickle_dict             | 27.6 us                                                | 30.0 us: 1.09x slower                                                      |
| python_startup_no_site  | 5.78 ms                                                | 6.48 ms: 1.12x slower                                                      |
| dask                    | 436 ms                                                 | 503 ms: 1.15x slower                                                       |
| coverage                | 74.7 ms                                                | 91.6 ms: 1.22x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                               |

Benchmark hidden because not significant (4): bench_mp_pool, pickle, unpickle, mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-76326f3/bm-20230316-linux-x86_64-faster%2dcpython-no_deep_freeze-3.12.0a6+-76326f3.json: comprehensions
