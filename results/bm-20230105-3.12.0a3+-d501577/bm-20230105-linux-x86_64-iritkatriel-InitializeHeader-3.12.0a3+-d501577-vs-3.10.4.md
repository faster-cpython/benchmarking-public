
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 252 ms: 1.33x faster                                                    |
| chameleon      | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                   |
| docutils       | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                  |
| html5lib       | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.4 ms: 1.54x faster                                                   |
| float          | 109 ms                                                 | 71.9 ms: 1.52x faster                                                   |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| regex_dna      | 214 ms                                                 | 208 ms: 1.03x faster                                                    |
| regex_effbot   | 3.19 ms                                                | 3.60 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                                    |
| unpickle_pure_python | 302 us                                                 | 199 us: 1.51x faster                                                    |
| json_dumps           | 13.4 ms                                                | 9.36 ms: 1.44x faster                                                   |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| xml_etree_generate   | 93.8 ms                                                | 77.0 ms: 1.22x faster                                                   |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                   |
| pickle_list          | 4.72 us                                                | 4.00 us: 1.18x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| unpickle             | 14.2 us                                                | 13.0 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                    |
| pickle               | 10.2 us                                                | 9.96 us: 1.02x faster                                                   |
| pickle_dict          | 27.6 us                                                | 29.8 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                   |
| python_startup_no_site | 5.78 ms                                                | 6.07 ms: 1.05x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                   |
| genshi_text     | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                   |
| django_template | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                   |
| genshi_xml      | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.23 ms: 2.25x faster                                                   |
| logging_silent          | 176 ns                                                 | 92.5 ns: 1.91x faster                                                   |
| richards                | 75.2 ms                                                | 41.3 ms: 1.82x faster                                                   |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                    |
| pyflate                 | 676 ms                                                 | 401 ms: 1.69x faster                                                    |
| go                      | 226 ms                                                 | 134 ms: 1.68x faster                                                    |
| scimark_monte_carlo     | 109 ms                                                 | 64.6 ms: 1.68x faster                                                   |
| python_startup          | 14.1 ms                                                | 8.48 ms: 1.66x faster                                                   |
| raytrace                | 467 ms                                                 | 284 ms: 1.64x faster                                                    |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                                    |
| crypto_pyaes            | 117 ms                                                 | 74.3 ms: 1.57x faster                                                   |
| chaos                   | 106 ms                                                 | 67.5 ms: 1.56x faster                                                   |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                   |
| hexiom                  | 9.43 ms                                                | 6.06 ms: 1.55x faster                                                   |
| nbody                   | 144 ms                                                 | 93.4 ms: 1.54x faster                                                   |
| float                   | 109 ms                                                 | 71.9 ms: 1.52x faster                                                   |
| unpickle_pure_python    | 302 us                                                 | 199 us: 1.51x faster                                                    |
| mako                    | 14.7 ms                                                | 9.71 ms: 1.51x faster                                                   |
| genshi_text             | 30.6 ms                                                | 20.3 ms: 1.51x faster                                                   |
| deepcopy_memo           | 51.7 us                                                | 34.4 us: 1.50x faster                                                   |
| scimark_lu              | 161 ms                                                 | 108 ms: 1.49x faster                                                    |
| chameleon               | 9.17 ms                                                | 6.23 ms: 1.47x faster                                                   |
| sqlglot_parse           | 2.04 ms                                                | 1.40 ms: 1.46x faster                                                   |
| sqlglot_transpile       | 2.43 ms                                                | 1.69 ms: 1.44x faster                                                   |
| pprint_pformat          | 1.98 sec                                               | 1.38 sec: 1.44x faster                                                  |
| json_dumps              | 13.4 ms                                                | 9.36 ms: 1.44x faster                                                   |
| html5lib                | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                   |
| django_template         | 46.3 ms                                                | 32.7 ms: 1.42x faster                                                   |
| logging_simple          | 8.10 us                                                | 5.72 us: 1.42x faster                                                   |
| pprint_safe_repr        | 953 ms                                                 | 674 ms: 1.41x faster                                                    |
| unpack_sequence         | 59.4 ns                                                | 42.5 ns: 1.40x faster                                                   |
| logging_format          | 8.85 us                                                | 6.35 us: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 743 us: 1.39x faster                                                    |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                    |
| genshi_xml              | 63.7 ms                                                | 46.6 ms: 1.37x faster                                                   |
| scimark_fft             | 421 ms                                                 | 310 ms: 1.36x faster                                                    |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                                    |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                                  |
| fannkuch                | 488 ms                                                 | 363 ms: 1.34x faster                                                    |
| async_tree_memoization  | 855 ms                                                 | 638 ms: 1.34x faster                                                    |
| 2to3                    | 335 ms                                                 | 252 ms: 1.33x faster                                                    |
| pycparser               | 1.53 sec                                               | 1.15 sec: 1.33x faster                                                  |
| deepcopy                | 438 us                                                 | 334 us: 1.31x faster                                                    |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.79 us                                                | 2.97 us: 1.28x faster                                                   |
| docutils                | 3.18 sec                                               | 2.49 sec: 1.27x faster                                                  |
| sqlglot_normalize       | 134 ms                                                 | 106 ms: 1.27x faster                                                    |
| coroutines              | 31.6 ms                                                | 25.0 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed | 949 ms                                                 | 758 ms: 1.25x faster                                                    |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                   |
| dulwich_log             | 75.8 ms                                                | 62.0 ms: 1.22x faster                                                   |
| xml_etree_generate      | 93.8 ms                                                | 77.0 ms: 1.22x faster                                                   |
| bench_thread_pool       | 946 us                                                 | 777 us: 1.22x faster                                                    |
| async_generators        | 426 ms                                                 | 352 ms: 1.21x faster                                                    |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                   |
| sympy_integrate         | 24.0 ms                                                | 20.3 ms: 1.18x faster                                                   |
| pickle_list             | 4.72 us                                                | 4.00 us: 1.18x faster                                                   |
| sympy_expand            | 534 ms                                                 | 455 ms: 1.17x faster                                                    |
| sympy_str               | 325 ms                                                 | 281 ms: 1.16x faster                                                    |
| json                    | 5.35 ms                                                | 4.69 ms: 1.14x faster                                                   |
| djangocms               | 36.9 us                                                | 32.6 us: 1.13x faster                                                   |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                                   |
| sympy_sum               | 183 ms                                                 | 163 ms: 1.13x faster                                                    |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                   |
| meteor_contest          | 114 ms                                                 | 104 ms: 1.09x faster                                                    |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| unpickle                | 14.2 us                                                | 13.0 us: 1.09x faster                                                   |
| telco                   | 6.73 ms                                                | 6.36 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                    |
| regex_dna               | 214 ms                                                 | 208 ms: 1.03x faster                                                    |
| pickle                  | 10.2 us                                                | 9.96 us: 1.02x faster                                                   |
| generators              | 76.4 ms                                                | 75.4 ms: 1.01x faster                                                   |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| python_startup_no_site  | 5.78 ms                                                | 6.07 ms: 1.05x slower                                                   |
| pickle_dict             | 27.6 us                                                | 29.8 us: 1.08x slower                                                   |
| regex_effbot            | 3.19 ms                                                | 3.60 ms: 1.13x slower                                                   |
| coverage                | 74.7 ms                                                | 100 ms: 1.34x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                            |

Benchmark hidden because not significant (3): mdp, bench_mp_pool, unpickle_list
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230105-3.12.0a3+-d501577/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577.json: mypy
