
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                    |
| chameleon      | 8.86 ms                                                | 6.23 ms: 1.42x faster                                                   |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                  |
| html5lib       | 85.8 ms                                                | 59.9 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.9 ms: 1.50x faster                                                   |
| nbody          | 136 ms                                                 | 93.4 ms: 1.46x faster                                                   |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.28x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.34x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                    |
| regex_effbot   | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 283 us: 1.60x faster                                                    |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                    |
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| xml_etree_generate   | 93.3 ms                                                | 77.0 ms: 1.21x faster                                                   |
| json_loads           | 28.9 us                                                | 23.9 us: 1.21x faster                                                   |
| pickle_list          | 4.50 us                                                | 4.00 us: 1.13x faster                                                   |
| unpickle             | 14.3 us                                                | 13.0 us: 1.10x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                 | 107 ms: 1.03x faster                                                    |
| pickle               | 10.1 us                                                | 9.96 us: 1.02x faster                                                   |
| unpickle_list        | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| pickle_dict          | 28.3 us                                                | 29.8 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                   |
| python_startup_no_site | 5.76 ms                                                | 6.07 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                   |
| mako            | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                   |
| django_template | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                   |
| genshi_xml      | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.23 ms: 2.29x faster                                                   |
| logging_silent          | 173 ns                                                 | 92.5 ns: 1.87x faster                                                   |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.79x faster                                                    |
| richards                | 71.4 ms                                                | 41.3 ms: 1.73x faster                                                   |
| go                      | 226 ms                                                 | 134 ms: 1.69x faster                                                    |
| pyflate                 | 675 ms                                                 | 401 ms: 1.69x faster                                                    |
| python_startup          | 13.9 ms                                                | 8.48 ms: 1.64x faster                                                   |
| raytrace                | 461 ms                                                 | 284 ms: 1.62x faster                                                    |
| scimark_monte_carlo     | 105 ms                                                 | 64.6 ms: 1.62x faster                                                   |
| pickle_pure_python      | 453 us                                                 | 283 us: 1.60x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.58x faster                                                   |
| hexiom                  | 9.42 ms                                                | 6.06 ms: 1.55x faster                                                   |
| spectral_norm           | 148 ms                                                 | 95.9 ms: 1.54x faster                                                   |
| chaos                   | 104 ms                                                 | 67.5 ms: 1.54x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                   |
| float                   | 108 ms                                                 | 71.9 ms: 1.50x faster                                                   |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                    |
| mako                    | 14.3 ms                                                | 9.71 ms: 1.47x faster                                                   |
| scimark_lu              | 158 ms                                                 | 108 ms: 1.46x faster                                                    |
| nbody                   | 136 ms                                                 | 93.4 ms: 1.46x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.45x faster                                                   |
| deepcopy_memo           | 50.0 us                                                | 34.4 us: 1.45x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.44x faster                                                   |
| html5lib                | 85.8 ms                                                | 59.9 ms: 1.43x faster                                                   |
| pprint_pformat          | 1.97 sec                                               | 1.38 sec: 1.43x faster                                                  |
| sqlglot_transpile       | 2.42 ms                                                | 1.69 ms: 1.43x faster                                                   |
| chameleon               | 8.86 ms                                                | 6.23 ms: 1.42x faster                                                   |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                   |
| logging_simple          | 8.06 us                                                | 5.72 us: 1.41x faster                                                   |
| logging_format          | 8.92 us                                                | 6.35 us: 1.41x faster                                                   |
| unpack_sequence         | 59.5 ns                                                | 42.5 ns: 1.40x faster                                                   |
| pprint_safe_repr        | 943 ms                                                 | 674 ms: 1.40x faster                                                    |
| thrift                  | 1.03 ms                                                | 743 us: 1.39x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.98 ms: 1.38x faster                                                   |
| genshi_xml              | 63.6 ms                                                | 46.6 ms: 1.36x faster                                                   |
| async_tree_none         | 713 ms                                                 | 527 ms: 1.35x faster                                                    |
| regex_compile           | 174 ms                                                 | 129 ms: 1.34x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.34x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 638 ms: 1.34x faster                                                    |
| scimark_fft             | 414 ms                                                 | 310 ms: 1.33x faster                                                    |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                    |
| fannkuch                | 477 ms                                                 | 363 ms: 1.31x faster                                                    |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                                  |
| deepcopy                | 429 us                                                 | 334 us: 1.29x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                   |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.28x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.27x faster                                                    |
| coroutines              | 31.7 ms                                                | 25.0 ms: 1.27x faster                                                   |
| deepcopy_reduce         | 3.75 us                                                | 2.97 us: 1.26x faster                                                   |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                    |
| nqueens                 | 99.3 ms                                                | 80.8 ms: 1.23x faster                                                   |
| dulwich_log             | 75.5 ms                                                | 62.0 ms: 1.22x faster                                                   |
| async_generators        | 428 ms                                                 | 352 ms: 1.22x faster                                                    |
| bench_thread_pool       | 943 us                                                 | 777 us: 1.21x faster                                                    |
| xml_etree_generate      | 93.3 ms                                                | 77.0 ms: 1.21x faster                                                   |
| json_loads              | 28.9 us                                                | 23.9 us: 1.21x faster                                                   |
| sympy_expand            | 537 ms                                                 | 455 ms: 1.18x faster                                                    |
| sympy_integrate         | 23.9 ms                                                | 20.3 ms: 1.18x faster                                                   |
| sympy_str               | 324 ms                                                 | 281 ms: 1.16x faster                                                    |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                    |
| pickle_list             | 4.50 us                                                | 4.00 us: 1.13x faster                                                   |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                   |
| unpickle                | 14.3 us                                                | 13.0 us: 1.10x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                    |
| telco                   | 6.68 ms                                                | 6.36 ms: 1.05x faster                                                   |
| xml_etree_iterparse     | 110 ms                                                 | 107 ms: 1.03x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.74 sec: 1.03x faster                                                  |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                    |
| pickle                  | 10.1 us                                                | 9.96 us: 1.02x faster                                                   |
| unpickle_list           | 4.99 us                                                | 4.94 us: 1.01x faster                                                   |
| generators              | 75.8 ms                                                | 75.4 ms: 1.00x faster                                                   |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| python_startup_no_site  | 5.76 ms                                                | 6.07 ms: 1.05x slower                                                   |
| pickle_dict             | 28.3 us                                                | 29.8 us: 1.05x slower                                                   |
| regex_effbot            | 3.21 ms                                                | 3.60 ms: 1.12x slower                                                   |
| coverage                | 75.3 ms                                                | 100 ms: 1.33x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20230105-3.12.0a3+-d501577/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577.json: djangocms
