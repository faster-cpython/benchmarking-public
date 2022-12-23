Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 253 ms: 1.02x faster                                                        |
| docutils       | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                      |
| html5lib       | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.3 ms: 1.06x faster                                                       |
| nbody          | 95.0 ms                                                | 93.6 ms: 1.02x faster                                                       |
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| regex_dna      | 203 ms                                                 | 219 ms: 1.08x slower                                                        |
| regex_effbot   | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                       |
| regex_v8       | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.49 ms: 1.33x faster                                                       |
| json_loads           | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| pickle               | 9.79 us                                                | 10.2 us: 1.05x slower                                                       |
| pickle_dict          | 31.4 us                                                | 30.6 us: 1.03x faster                                                       |
| pickle_list          | 4.17 us                                                | 4.12 us: 1.01x faster                                                       |
| pickle_pure_python   | 304 us                                                 | 282 us: 1.08x faster                                                        |
| unpickle_list        | 4.95 us                                                | 5.12 us: 1.03x slower                                                       |
| unpickle_pure_python | 225 us                                                 | 199 us: 1.13x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.50 ms: 1.02x slower                                                       |
| python_startup_no_site | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 32.9 ms: 1.02x slower                                                       |
| genshi_text     | 22.1 ms                                                | 21.3 ms: 1.04x faster                                                       |
| genshi_xml      | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                       |
| mako            | 9.85 ms                                                | 9.72 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 253 ms: 1.02x faster                                                        |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed | 752 ms                                                 | 765 ms: 1.02x slower                                                        |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                                      |
| chaos                   | 68.6 ms                                                | 66.1 ms: 1.04x faster                                                       |
| bench_thread_pool       | 810 us                                                 | 774 us: 1.05x faster                                                        |
| coroutines              | 26.1 ms                                                | 25.0 ms: 1.05x faster                                                       |
| coverage                | 101 ms                                                 | 99.4 ms: 1.01x faster                                                       |
| deepcopy                | 344 us                                                 | 326 us: 1.05x faster                                                        |
| deepcopy_reduce         | 2.97 us                                                | 2.88 us: 1.03x faster                                                       |
| deepcopy_memo           | 36.4 us                                                | 33.5 us: 1.09x faster                                                       |
| deltablue               | 3.64 ms                                                | 3.22 ms: 1.13x faster                                                       |
| django_template         | 32.5 ms                                                | 32.9 ms: 1.02x slower                                                       |
| docutils                | 2.60 sec                                               | 2.49 sec: 1.04x faster                                                      |
| dulwich_log             | 63.9 ms                                                | 62.0 ms: 1.03x faster                                                       |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                                        |
| float                   | 76.3 ms                                                | 72.3 ms: 1.06x faster                                                       |
| generators              | 72.2 ms                                                | 77.6 ms: 1.07x slower                                                       |
| genshi_text             | 22.1 ms                                                | 21.3 ms: 1.04x faster                                                       |
| genshi_xml              | 52.1 ms                                                | 47.0 ms: 1.11x faster                                                       |
| go                      | 143 ms                                                 | 135 ms: 1.06x faster                                                        |
| hexiom                  | 6.35 ms                                                | 6.08 ms: 1.04x faster                                                       |
| html5lib                | 63.2 ms                                                | 59.7 ms: 1.06x faster                                                       |
| json                    | 4.95 ms                                                | 4.80 ms: 1.03x faster                                                       |
| json_dumps              | 12.7 ms                                                | 9.49 ms: 1.33x faster                                                       |
| json_loads              | 26.2 us                                                | 24.0 us: 1.09x faster                                                       |
| logging_format          | 6.62 us                                                | 6.28 us: 1.05x faster                                                       |
| logging_silent          | 98.5 ns                                                | 92.1 ns: 1.07x faster                                                       |
| logging_simple          | 6.06 us                                                | 5.69 us: 1.07x faster                                                       |
| mako                    | 9.85 ms                                                | 9.72 ms: 1.01x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                      |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                                        |
| mypy                    | 669 ms                                                 | 804 ms: 1.20x slower                                                        |
| nbody                   | 95.0 ms                                                | 93.6 ms: 1.02x faster                                                       |
| nqueens                 | 85.0 ms                                                | 78.5 ms: 1.08x faster                                                       |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                       |
| pickle                  | 9.79 us                                                | 10.2 us: 1.05x slower                                                       |
| pickle_dict             | 31.4 us                                                | 30.6 us: 1.03x faster                                                       |
| pickle_list             | 4.17 us                                                | 4.12 us: 1.01x faster                                                       |
| pickle_pure_python      | 304 us                                                 | 282 us: 1.08x faster                                                        |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 691 ms                                                 | 677 ms: 1.02x faster                                                        |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                                      |
| pycparser               | 1.17 sec                                               | 1.13 sec: 1.04x faster                                                      |
| pyflate                 | 417 ms                                                 | 407 ms: 1.03x faster                                                        |
| python_startup          | 8.36 ms                                                | 8.50 ms: 1.02x slower                                                       |
| python_startup_no_site  | 5.96 ms                                                | 6.08 ms: 1.02x slower                                                       |
| raytrace                | 290 ms                                                 | 280 ms: 1.04x faster                                                        |
| regex_compile           | 136 ms                                                 | 130 ms: 1.05x faster                                                        |
| regex_dna               | 203 ms                                                 | 219 ms: 1.08x slower                                                        |
| regex_effbot            | 3.36 ms                                                | 3.58 ms: 1.07x slower                                                       |
| regex_v8                | 22.3 ms                                                | 22.2 ms: 1.01x faster                                                       |
| richards                | 46.2 ms                                                | 41.6 ms: 1.11x faster                                                       |
| scimark_fft             | 329 ms                                                 | 315 ms: 1.04x faster                                                        |
| scimark_lu              | 107 ms                                                 | 106 ms: 1.01x faster                                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 66.1 ms: 1.03x faster                                                       |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.03 ms: 1.09x faster                                                       |
| spectral_norm           | 99.9 ms                                                | 96.1 ms: 1.04x faster                                                       |
| sqlglot_parse           | 1.37 ms                                                | 1.39 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.66 ms                                                | 1.69 ms: 1.02x slower                                                       |
| sqlglot_optimize        | 53.0 ms                                                | 50.5 ms: 1.05x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| sqlite_synth            | 2.49 us                                                | 2.56 us: 1.03x slower                                                       |
| sympy_expand            | 472 ms                                                 | 449 ms: 1.05x faster                                                        |
| sympy_integrate         | 20.9 ms                                                | 20.2 ms: 1.03x faster                                                       |
| sympy_sum               | 166 ms                                                 | 161 ms: 1.03x faster                                                        |
| sympy_str               | 287 ms                                                 | 282 ms: 1.02x faster                                                        |
| telco                   | 6.62 ms                                                | 6.17 ms: 1.07x faster                                                       |
| thrift                  | 752 us                                                 | 745 us: 1.01x faster                                                        |
| unpack_sequence         | 43.4 ns                                                | 41.6 ns: 1.04x faster                                                       |
| unpickle_list           | 4.95 us                                                | 5.12 us: 1.03x slower                                                       |
| unpickle_pure_python    | 225 us                                                 | 199 us: 1.13x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (8): async_tree_none, async_tree_memoization, chameleon, bench_mp_pool, crypto_pyaes, unpickle, xml_etree_iterparse, xml_etree_process
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: djangocms
