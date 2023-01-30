
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 15497c4
- commit date: 2023-01-17
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 258 ms: 1.29x faster                                              |
| chameleon      | 8.86 ms                                                | 6.52 ms: 1.36x faster                                             |
| docutils       | 3.18 sec                                               | 2.60 sec: 1.22x faster                                            |
| html5lib       | 85.8 ms                                                | 60.9 ms: 1.41x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.5 ms: 1.46x faster                                             |
| nbody          | 136 ms                                                 | 95.6 ms: 1.43x faster                                             |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.28x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 135 ms: 1.29x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| regex_dna      | 214 ms                                                 | 219 ms: 1.03x slower                                              |
| regex_effbot   | 3.21 ms                                                | 3.60 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 295 us: 1.53x faster                                              |
| unpickle_pure_python | 297 us                                                 | 207 us: 1.43x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.59 ms: 1.41x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 54.7 ms: 1.36x faster                                             |
| xml_etree_generate   | 93.3 ms                                                | 78.3 ms: 1.19x faster                                             |
| json_loads           | 28.9 us                                                | 24.5 us: 1.18x faster                                             |
| pickle_list          | 4.50 us                                                | 4.06 us: 1.11x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                              |
| unpickle             | 14.3 us                                                | 13.3 us: 1.07x faster                                             |
| unpickle_list        | 4.99 us                                                | 4.92 us: 1.01x faster                                             |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                             |
| pickle_dict          | 28.3 us                                                | 30.8 us: 1.09x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.59 ms: 1.62x faster                                             |
| python_startup_no_site | 5.76 ms                                                | 6.10 ms: 1.06x slower                                             |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.9 ms: 1.46x faster                                             |
| mako            | 14.3 ms                                                | 9.77 ms: 1.46x faster                                             |
| django_template | 46.3 ms                                                | 33.9 ms: 1.37x faster                                             |
| genshi_xml      | 63.6 ms                                                | 48.4 ms: 1.31x faster                                             |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.38 ms: 2.19x faster                                             |
| scimark_sor             | 193 ms                                                 | 109 ms: 1.77x faster                                              |
| logging_silent          | 173 ns                                                 | 97.7 ns: 1.77x faster                                             |
| pyflate                 | 675 ms                                                 | 411 ms: 1.64x faster                                              |
| richards                | 71.4 ms                                                | 43.8 ms: 1.63x faster                                             |
| go                      | 226 ms                                                 | 139 ms: 1.63x faster                                              |
| python_startup          | 13.9 ms                                                | 8.59 ms: 1.62x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 74.7 ms: 1.57x faster                                             |
| chaos                   | 104 ms                                                 | 67.2 ms: 1.55x faster                                             |
| scimark_monte_carlo     | 105 ms                                                 | 68.1 ms: 1.54x faster                                             |
| raytrace                | 461 ms                                                 | 301 ms: 1.53x faster                                              |
| pickle_pure_python      | 453 us                                                 | 295 us: 1.53x faster                                              |
| spectral_norm           | 148 ms                                                 | 97.9 ms: 1.51x faster                                             |
| hexiom                  | 9.42 ms                                                | 6.25 ms: 1.51x faster                                             |
| float                   | 108 ms                                                 | 73.5 ms: 1.46x faster                                             |
| genshi_text             | 30.6 ms                                                | 20.9 ms: 1.46x faster                                             |
| mako                    | 14.3 ms                                                | 9.77 ms: 1.46x faster                                             |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.44x faster                                              |
| unpickle_pure_python    | 297 us                                                 | 207 us: 1.43x faster                                              |
| nbody                   | 136 ms                                                 | 95.6 ms: 1.43x faster                                             |
| deepcopy_memo           | 50.0 us                                                | 35.2 us: 1.42x faster                                             |
| unpack_sequence         | 59.5 ns                                                | 41.9 ns: 1.42x faster                                             |
| html5lib                | 85.8 ms                                                | 60.9 ms: 1.41x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.59 ms: 1.41x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                             |
| pprint_pformat          | 1.97 sec                                               | 1.42 sec: 1.39x faster                                            |
| thrift                  | 1.03 ms                                                | 751 us: 1.37x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.76 ms: 1.37x faster                                             |
| django_template         | 46.3 ms                                                | 33.9 ms: 1.37x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 54.7 ms: 1.36x faster                                             |
| logging_simple          | 8.06 us                                                | 5.92 us: 1.36x faster                                             |
| chameleon               | 8.86 ms                                                | 6.52 ms: 1.36x faster                                             |
| pprint_safe_repr        | 943 ms                                                 | 695 ms: 1.36x faster                                              |
| logging_format          | 8.92 us                                                | 6.59 us: 1.35x faster                                             |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.06 ms: 1.35x faster                                             |
| async_tree_none         | 713 ms                                                 | 528 ms: 1.35x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                            |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.32x faster                                            |
| genshi_xml              | 63.6 ms                                                | 48.4 ms: 1.31x faster                                             |
| scimark_fft             | 414 ms                                                 | 316 ms: 1.31x faster                                              |
| 2to3                    | 332 ms                                                 | 258 ms: 1.29x faster                                              |
| regex_compile           | 174 ms                                                 | 135 ms: 1.29x faster                                              |
| async_tree_memoization  | 854 ms                                                 | 670 ms: 1.28x faster                                              |
| fannkuch                | 477 ms                                                 | 380 ms: 1.26x faster                                              |
| deepcopy                | 429 us                                                 | 345 us: 1.25x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 762 ms: 1.25x faster                                              |
| nqueens                 | 99.3 ms                                                | 79.9 ms: 1.24x faster                                             |
| deepcopy_reduce         | 3.75 us                                                | 3.02 us: 1.24x faster                                             |
| sqlglot_optimize        | 65.3 ms                                                | 53.0 ms: 1.23x faster                                             |
| docutils                | 3.18 sec                                               | 2.60 sec: 1.22x faster                                            |
| sqlglot_normalize       | 135 ms                                                 | 110 ms: 1.22x faster                                              |
| async_generators        | 428 ms                                                 | 353 ms: 1.21x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 78.3 ms: 1.19x faster                                             |
| bench_thread_pool       | 943 us                                                 | 795 us: 1.19x faster                                              |
| coroutines              | 31.7 ms                                                | 26.8 ms: 1.18x faster                                             |
| mypy                    | 1.01 sec                                               | 860 ms: 1.18x faster                                              |
| json_loads              | 28.9 us                                                | 24.5 us: 1.18x faster                                             |
| dulwich_log             | 75.5 ms                                                | 64.1 ms: 1.18x faster                                             |
| json                    | 5.35 ms                                                | 4.67 ms: 1.15x faster                                             |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                            |
| sympy_expand            | 537 ms                                                 | 475 ms: 1.13x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                             |
| sympy_str               | 324 ms                                                 | 291 ms: 1.11x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| pickle_list             | 4.50 us                                                | 4.06 us: 1.11x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                              |
| sympy_integrate         | 23.9 ms                                                | 22.1 ms: 1.08x faster                                             |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                              |
| unpickle                | 14.3 us                                                | 13.3 us: 1.07x faster                                             |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                              |
| telco                   | 6.68 ms                                                | 6.35 ms: 1.05x faster                                             |
| unpickle_list           | 4.99 us                                                | 4.92 us: 1.01x faster                                             |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                              |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                             |
| generators              | 75.8 ms                                                | 77.6 ms: 1.02x slower                                             |
| regex_dna               | 214 ms                                                 | 219 ms: 1.03x slower                                              |
| python_startup_no_site  | 5.76 ms                                                | 6.10 ms: 1.06x slower                                             |
| pickle_dict             | 28.3 us                                                | 30.8 us: 1.09x slower                                             |
| regex_effbot            | 3.21 ms                                                | 3.60 ms: 1.12x slower                                             |
| coverage                | 75.3 ms                                                | 99.1 ms: 1.31x slower                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
