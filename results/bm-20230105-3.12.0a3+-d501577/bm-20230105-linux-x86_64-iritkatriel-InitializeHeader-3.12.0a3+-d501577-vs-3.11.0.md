
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 252 ms: 1.02x faster                                                    |
| chameleon      | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                   |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                  |
| html5lib       | 63.2 ms                                                | 59.9 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 71.9 ms: 1.06x faster                                                   |
| nbody          | 95.0 ms                                                | 93.4 ms: 1.02x faster                                                   |
| pidigits       | 199 ms                                                 | 198 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.05x faster                                                    |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                   |
| regex_dna      | 203 ms                                                 | 208 ms: 1.02x slower                                                    |
| regex_effbot   | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                   |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                    |
| json_loads           | 26.2 us                                                | 23.9 us: 1.10x faster                                                   |
| pickle_pure_python   | 304 us                                                 | 283 us: 1.07x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                    |
| pickle_dict          | 31.4 us                                                | 29.8 us: 1.05x faster                                                   |
| pickle_list          | 4.17 us                                                | 4.00 us: 1.04x faster                                                   |
| xml_etree_generate   | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                   |
| pickle               | 9.79 us                                                | 9.96 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 103 ms                                                 | 107 ms: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                            |

Benchmark hidden because not significant (3): unpickle, unpickle_list, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.48 ms: 1.01x slower                                                   |
| python_startup_no_site | 5.96 ms                                                | 6.07 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                   |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                   |
| mako            | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                   |
| django_template | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.36 ms: 1.35x faster                                                   |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                    |
| deltablue               | 3.64 ms                                                | 3.23 ms: 1.13x faster                                                   |
| richards                | 46.2 ms                                                | 41.3 ms: 1.12x faster                                                   |
| genshi_xml              | 52.1 ms                                                | 46.6 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.98 ms: 1.11x faster                                                   |
| json_loads              | 26.2 us                                                | 23.9 us: 1.10x faster                                                   |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                   |
| pickle_pure_python      | 304 us                                                 | 283 us: 1.07x faster                                                    |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                    |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                                    |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                                    |
| logging_silent          | 98.5 ns                                                | 92.5 ns: 1.06x faster                                                   |
| float                   | 76.3 ms                                                | 71.9 ms: 1.06x faster                                                   |
| deepcopy_memo           | 36.4 us                                                | 34.4 us: 1.06x faster                                                   |
| scimark_fft             | 329 ms                                                 | 310 ms: 1.06x faster                                                    |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                    |
| logging_simple          | 6.06 us                                                | 5.72 us: 1.06x faster                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 64.6 ms: 1.06x faster                                                   |
| json                    | 4.95 ms                                                | 4.69 ms: 1.06x faster                                                   |
| html5lib                | 63.2 ms                                                | 59.9 ms: 1.05x faster                                                   |
| pickle_dict             | 31.4 us                                                | 29.8 us: 1.05x faster                                                   |
| nqueens                 | 85.0 ms                                                | 80.8 ms: 1.05x faster                                                   |
| regex_compile           | 136 ms                                                 | 129 ms: 1.05x faster                                                    |
| hexiom                  | 6.35 ms                                                | 6.06 ms: 1.05x faster                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.38 sec: 1.05x faster                                                  |
| pickle_list             | 4.17 us                                                | 4.00 us: 1.04x faster                                                   |
| coroutines              | 26.1 ms                                                | 25.0 ms: 1.04x faster                                                   |
| bench_thread_pool       | 810 us                                                 | 777 us: 1.04x faster                                                    |
| spectral_norm           | 99.9 ms                                                | 95.9 ms: 1.04x faster                                                   |
| logging_format          | 6.62 us                                                | 6.35 us: 1.04x faster                                                   |
| telco                   | 6.62 ms                                                | 6.36 ms: 1.04x faster                                                   |
| pyflate                 | 417 ms                                                 | 401 ms: 1.04x faster                                                    |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 51.0 ms: 1.04x faster                                                   |
| sympy_expand            | 472 ms                                                 | 455 ms: 1.04x faster                                                    |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                   |
| deepcopy                | 344 us                                                 | 334 us: 1.03x faster                                                    |
| chameleon               | 6.41 ms                                                | 6.23 ms: 1.03x faster                                                   |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 674 ms: 1.02x faster                                                    |
| sympy_str               | 287 ms                                                 | 281 ms: 1.02x faster                                                    |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                                    |
| 2to3                    | 257 ms                                                 | 252 ms: 1.02x faster                                                    |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                    |
| unpack_sequence         | 43.4 ns                                                | 42.5 ns: 1.02x faster                                                   |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                  |
| sympy_sum               | 166 ms                                                 | 163 ms: 1.02x faster                                                    |
| nbody                   | 95.0 ms                                                | 93.4 ms: 1.02x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                    |
| chaos                   | 68.6 ms                                                | 67.5 ms: 1.02x faster                                                   |
| mako                    | 9.85 ms                                                | 9.71 ms: 1.01x faster                                                   |
| thrift                  | 752 us                                                 | 743 us: 1.01x faster                                                    |
| pidigits                | 199 ms                                                 | 198 ms: 1.01x faster                                                    |
| crypto_pyaes            | 73.9 ms                                                | 74.3 ms: 1.01x slower                                                   |
| django_template         | 32.5 ms                                                | 32.7 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 758 ms: 1.01x slower                                                    |
| xml_etree_generate      | 76.2 ms                                                | 77.0 ms: 1.01x slower                                                   |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                   |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                  |
| python_startup          | 8.36 ms                                                | 8.48 ms: 1.01x slower                                                   |
| pickle                  | 9.79 us                                                | 9.96 us: 1.02x slower                                                   |
| python_startup_no_site  | 5.96 ms                                                | 6.07 ms: 1.02x slower                                                   |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                   |
| async_tree_memoization  | 625 ms                                                 | 638 ms: 1.02x slower                                                    |
| sqlglot_parse           | 1.37 ms                                                | 1.40 ms: 1.02x slower                                                   |
| regex_dna               | 203 ms                                                 | 208 ms: 1.02x slower                                                    |
| xml_etree_iterparse     | 103 ms                                                 | 107 ms: 1.04x slower                                                    |
| sqlite_synth            | 2.49 us                                                | 2.59 us: 1.04x slower                                                   |
| mdp                     | 2.62 sec                                               | 2.74 sec: 1.04x slower                                                  |
| generators              | 72.2 ms                                                | 75.4 ms: 1.05x slower                                                   |
| regex_effbot            | 3.36 ms                                                | 3.60 ms: 1.07x slower                                                   |
| mypy                    | 669 ms                                                 | 807 ms: 1.21x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                            |

Benchmark hidden because not significant (10): unpickle, meteor_contest, async_tree_none, unpickle_list, coverage, xml_etree_process, bench_mp_pool, pathlib, deepcopy_reduce, scimark_lu
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/mdboom/Work/builds/benchmarking/results/bm-20230105-3.12.0a3+-d501577/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577.json: djangocms
