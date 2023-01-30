
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 254 ms: 1.31x faster                                                        |
| chameleon      | 8.86 ms                                                | 6.15 ms: 1.44x faster                                                       |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                      |
| html5lib       | 85.8 ms                                                | 60.0 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.0 ms: 1.48x faster                                                       |
| nbody          | 136 ms                                                 | 95.7 ms: 1.42x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 130 ms: 1.33x faster                                                        |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                       |
| regex_dna      | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| regex_effbot   | 3.21 ms                                                | 3.61 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                        |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.28 ms: 1.45x faster                                                       |
| xml_etree_process    | 74.5 ms                                                | 53.4 ms: 1.39x faster                                                       |
| xml_etree_generate   | 93.3 ms                                                | 76.5 ms: 1.22x faster                                                       |
| json_loads           | 28.9 us                                                | 23.7 us: 1.22x faster                                                       |
| pickle_list          | 4.50 us                                                | 4.04 us: 1.11x faster                                                       |
| unpickle             | 14.3 us                                                | 12.9 us: 1.11x faster                                                       |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| unpickle_list        | 4.99 us                                                | 4.96 us: 1.01x faster                                                       |
| pickle_dict          | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.49 ms: 1.64x faster                                                       |
| python_startup_no_site | 5.76 ms                                                | 6.08 ms: 1.05x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.38 ms: 1.52x faster                                                       |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| django_template | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                       |
| genshi_xml      | 63.6 ms                                                | 46.9 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.29 ms: 2.24x faster                                                       |
| logging_silent          | 173 ns                                                 | 92.5 ns: 1.87x faster                                                       |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.78x faster                                                        |
| pyflate                 | 675 ms                                                 | 392 ms: 1.72x faster                                                        |
| richards                | 71.4 ms                                                | 42.3 ms: 1.69x faster                                                       |
| go                      | 226 ms                                                 | 135 ms: 1.67x faster                                                        |
| python_startup          | 13.9 ms                                                | 8.49 ms: 1.64x faster                                                       |
| scimark_monte_carlo     | 105 ms                                                 | 64.1 ms: 1.63x faster                                                       |
| raytrace                | 461 ms                                                 | 287 ms: 1.61x faster                                                        |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.58x faster                                                       |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                        |
| chaos                   | 104 ms                                                 | 67.4 ms: 1.54x faster                                                       |
| hexiom                  | 9.42 ms                                                | 6.10 ms: 1.54x faster                                                       |
| spectral_norm           | 148 ms                                                 | 97.1 ms: 1.53x faster                                                       |
| mako                    | 14.3 ms                                                | 9.38 ms: 1.52x faster                                                       |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                       |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                                        |
| float                   | 108 ms                                                 | 73.0 ms: 1.48x faster                                                       |
| deepcopy_memo           | 50.0 us                                                | 33.9 us: 1.47x faster                                                       |
| json_dumps              | 13.5 ms                                                | 9.28 ms: 1.45x faster                                                       |
| unpack_sequence         | 59.5 ns                                                | 41.2 ns: 1.44x faster                                                       |
| pprint_pformat          | 1.97 sec                                               | 1.37 sec: 1.44x faster                                                      |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                                       |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.44x faster                                                        |
| chameleon               | 8.86 ms                                                | 6.15 ms: 1.44x faster                                                       |
| html5lib                | 85.8 ms                                                | 60.0 ms: 1.43x faster                                                       |
| nbody                   | 136 ms                                                 | 95.7 ms: 1.42x faster                                                       |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                                       |
| django_template         | 46.3 ms                                                | 32.8 ms: 1.41x faster                                                       |
| pprint_safe_repr        | 943 ms                                                 | 671 ms: 1.40x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 53.4 ms: 1.39x faster                                                       |
| logging_simple          | 8.06 us                                                | 5.78 us: 1.39x faster                                                       |
| logging_format          | 8.92 us                                                | 6.42 us: 1.39x faster                                                       |
| thrift                  | 1.03 ms                                                | 750 us: 1.37x faster                                                        |
| genshi_xml              | 63.6 ms                                                | 46.9 ms: 1.35x faster                                                       |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                      |
| regex_compile           | 174 ms                                                 | 130 ms: 1.33x faster                                                        |
| async_tree_memoization  | 854 ms                                                 | 647 ms: 1.32x faster                                                        |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                      |
| 2to3                    | 332 ms                                                 | 254 ms: 1.31x faster                                                        |
| scimark_fft             | 414 ms                                                 | 318 ms: 1.30x faster                                                        |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                        |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                        |
| sqlglot_optimize        | 65.3 ms                                                | 50.9 ms: 1.28x faster                                                       |
| deepcopy_reduce         | 3.75 us                                                | 2.93 us: 1.28x faster                                                       |
| nqueens                 | 99.3 ms                                                | 77.8 ms: 1.28x faster                                                       |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                                      |
| fannkuch                | 477 ms                                                 | 377 ms: 1.27x faster                                                        |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.36 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                        |
| mypy                    | 1.01 sec                                               | 812 ms: 1.25x faster                                                        |
| coroutines              | 31.7 ms                                                | 25.4 ms: 1.25x faster                                                       |
| xml_etree_generate      | 93.3 ms                                                | 76.5 ms: 1.22x faster                                                       |
| json_loads              | 28.9 us                                                | 23.7 us: 1.22x faster                                                       |
| async_generators        | 428 ms                                                 | 352 ms: 1.21x faster                                                        |
| bench_thread_pool       | 943 us                                                 | 779 us: 1.21x faster                                                        |
| dulwich_log             | 75.5 ms                                                | 62.8 ms: 1.20x faster                                                       |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                       |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                       |
| sympy_str               | 324 ms                                                 | 282 ms: 1.15x faster                                                        |
| sympy_sum               | 183 ms                                                 | 164 ms: 1.12x faster                                                        |
| sqlite_synth            | 2.90 us                                                | 2.60 us: 1.12x faster                                                       |
| pickle_list             | 4.50 us                                                | 4.04 us: 1.11x faster                                                       |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                       |
| unpickle                | 14.3 us                                                | 12.9 us: 1.11x faster                                                       |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                       |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                        |
| telco                   | 6.68 ms                                                | 6.30 ms: 1.06x faster                                                       |
| mdp                     | 2.82 sec                                               | 2.72 sec: 1.04x faster                                                      |
| regex_dna               | 214 ms                                                 | 207 ms: 1.03x faster                                                        |
| unpickle_list           | 4.99 us                                                | 4.96 us: 1.01x faster                                                       |
| generators              | 75.8 ms                                                | 76.8 ms: 1.01x slower                                                       |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| python_startup_no_site  | 5.76 ms                                                | 6.08 ms: 1.05x slower                                                       |
| pickle_dict             | 28.3 us                                                | 31.0 us: 1.09x slower                                                       |
| regex_effbot            | 3.21 ms                                                | 3.61 ms: 1.12x slower                                                       |
| coverage                | 75.3 ms                                                | 98.8 ms: 1.31x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                                |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20230105-3.12.0a3+-94fa28c/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c.json: djangocms
