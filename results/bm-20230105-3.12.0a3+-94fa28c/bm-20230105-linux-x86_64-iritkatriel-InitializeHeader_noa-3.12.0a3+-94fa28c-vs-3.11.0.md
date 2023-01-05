
# Results vs. 3.11.0

- fork: iritkatriel
- ref: InitializeHeader_noa
- machine: linux-x86_64
- commit hash: 94fa28c
- commit date: 2023-01-05
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 254 ms: 1.01x faster                                                        |
| chameleon      | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                       |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                      |
| html5lib       | 63.2 ms                                                | 60.0 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                       |
| pidigits       | 199 ms                                                 | 197 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.04x faster                                                        |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.61 ms: 1.07x slower                                                       |
| regex_v8       | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.28 ms: 1.36x faster                                                       |
| json_loads           | 26.2 us                                                | 23.7 us: 1.11x faster                                                       |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| pickle_dict          | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.04 us: 1.03x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 287 us: 1.06x faster                                                        |
| unpickle             | 13.3 us                                                | 12.9 us: 1.03x faster                                                       |
| unpickle_pure_python | 225 us                                                 | 197 us: 1.14x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                 | 102 ms: 1.01x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                       |
| xml_etree_process    | 53.8 ms                                                | 53.4 ms: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.49 ms: 1.02x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.8 ms: 1.01x slower                                                       |
| genshi_text     | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| genshi_xml      | 52.1 ms                                                | 46.9 ms: 1.11x faster                                                       |
| mako            | 9.85 ms                                                | 9.38 ms: 1.05x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 254 ms: 1.01x faster                                                        |
| async_generators        | 359 ms                                                 | 352 ms: 1.02x faster                                                        |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                      |
| async_tree_memoization  | 625 ms                                                 | 647 ms: 1.04x slower                                                        |
| chameleon               | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                       |
| chaos                   | 68.6 ms                                                | 67.4 ms: 1.02x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 779 us: 1.04x faster                                                        |
| coroutines              | 26.1 ms                                                | 25.4 ms: 1.03x faster                                                       |
| coverage                | 101 ms                                                 | 98.8 ms: 1.02x faster                                                       |
| crypto_pyaes            | 73.9 ms                                                | 74.4 ms: 1.01x slower                                                       |
| deepcopy                | 344 us                                                 | 330 us: 1.04x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.93 us: 1.01x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 33.9 us: 1.07x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.29 ms: 1.11x faster                                                       |
| django_template         | 32.5 ms                                                | 32.8 ms: 1.01x slower                                                       |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.03x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.8 ms: 1.02x faster                                                       |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                        |
| float                   | 76.3 ms                                                | 73.0 ms: 1.05x faster                                                       |
| generators              | 72.2 ms                                                | 76.8 ms: 1.06x slower                                                       |
| genshi_text             | 22.1 ms                                                | 20.3 ms: 1.09x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 46.9 ms: 1.11x faster                                                       |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                        |
| hexiom                  | 6.35 ms                                                | 6.10 ms: 1.04x faster                                                       |
| html5lib                | 63.2 ms                                                | 60.0 ms: 1.05x faster                                                       |
| json                    | 4.95 ms                                                | 4.60 ms: 1.08x faster                                                       |
| json_dumps              | 12.7 ms                                                | 9.28 ms: 1.36x faster                                                       |
| json_loads              | 26.2 us                                                | 23.7 us: 1.11x faster                                                       |
| logging_format          | 6.62 us                                                | 6.42 us: 1.03x faster                                                       |
| logging_silent          | 98.5 ns                                                | 92.5 ns: 1.06x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.78 us: 1.05x faster                                                       |
| mako                    | 9.85 ms                                                | 9.38 ms: 1.05x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.72 sec: 1.04x slower                                                      |
| meteor_contest          | 105 ms                                                 | 103 ms: 1.02x faster                                                        |
| mypy                    | 669 ms                                                 | 812 ms: 1.21x slower                                                        |
| nqueens                 | 85.0 ms                                                | 77.8 ms: 1.09x faster                                                       |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                                       |
| pickle_dict             | 31.4 us                                                | 31.0 us: 1.01x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.04 us: 1.03x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 287 us: 1.06x faster                                                        |
| pidigits                | 199 ms                                                 | 197 ms: 1.01x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 671 ms: 1.03x faster                                                        |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                                      |
| pycparser               | 1.17 sec                                               | 1.15 sec: 1.02x faster                                                      |
| pyflate                 | 417 ms                                                 | 392 ms: 1.06x faster                                                        |
| python_startup          | 8.36 ms                                                | 8.49 ms: 1.02x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                       |
| raytrace                | 290 ms                                                 | 287 ms: 1.01x faster                                                        |
| regex_compile           | 136 ms                                                 | 130 ms: 1.04x faster                                                        |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.61 ms: 1.07x slower                                                       |
| regex_v8                | 22.3 ms                                                | 22.5 ms: 1.01x slower                                                       |
| richards                | 46.2 ms                                                | 42.3 ms: 1.09x faster                                                       |
| scimark_fft             | 329 ms                                                 | 318 ms: 1.04x faster                                                        |
| scimark_lu              | 107 ms                                                 | 110 ms: 1.02x slower                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 64.1 ms: 1.07x faster                                                       |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.36 ms: 1.01x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 97.1 ms: 1.03x faster                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                                       |
| sqlglot_optimize        | 53.0 ms                                                | 50.9 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| sqlite_synth            | 2.49 us                                                | 2.60 us: 1.04x slower                                                       |
| sympy_expand            | 472 ms                                                 | 457 ms: 1.03x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 20.3 ms: 1.03x faster                                                       |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                                        |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                        |
| telco                   | 6.62 ms                                                | 6.30 ms: 1.05x faster                                                       |
| unpack_sequence         | 43.4 ns                                                | 41.2 ns: 1.05x faster                                                       |
| unpickle                | 13.3 us                                                | 12.9 us: 1.03x faster                                                       |
| unpickle_pure_python    | 225 us                                                 | 197 us: 1.14x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| xml_etree_iterparse     | 103 ms                                                 | 102 ms: 1.01x faster                                                        |
| xml_etree_generate      | 76.2 ms                                                | 76.5 ms: 1.00x slower                                                       |
| xml_etree_process       | 53.8 ms                                                | 53.4 ms: 1.01x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, async_tree_cpu_io_mixed, bench_mp_pool, nbody, pathlib, thrift, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230105-3.12.0a3+-94fa28c/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader_noa-3.12.0a3+-94fa28c.json: djangocms
