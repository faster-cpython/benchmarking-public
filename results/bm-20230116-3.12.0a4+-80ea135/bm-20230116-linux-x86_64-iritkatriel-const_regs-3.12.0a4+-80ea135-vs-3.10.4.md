
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 80ea135
- commit date: 2023-01-16
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 259 ms: 1.28x faster                                              |
| chameleon      | 8.86 ms                                                | 6.33 ms: 1.40x faster                                             |
| docutils       | 3.18 sec                                               | 2.62 sec: 1.21x faster                                            |
| html5lib       | 85.8 ms                                                | 61.5 ms: 1.39x faster                                             |
| Geometric mean | (ref)                                                  | 1.32x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 108 ms                                                 | 74.1 ms: 1.45x faster                                             |
| nbody          | 136 ms                                                 | 96.2 ms: 1.42x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 134 ms: 1.30x faster                                              |
| regex_dna      | 214 ms                                                 | 217 ms: 1.01x slower                                              |
| regex_effbot   | 3.21 ms                                                | 3.63 ms: 1.13x slower                                             |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.12x faster                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| json_loads           | 28.9 us                                                | 24.1 us: 1.20x faster                                             |
| pickle_dict          | 28.3 us                                                | 31.1 us: 1.10x slower                                             |
| pickle_list          | 4.50 us                                                | 4.07 us: 1.10x faster                                             |
| pickle_pure_python   | 453 us                                                 | 297 us: 1.53x faster                                              |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                             |
| unpickle_pure_python | 297 us                                                 | 203 us: 1.46x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.08x faster                                              |
| xml_etree_generate   | 93.3 ms                                                | 78.4 ms: 1.19x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 54.5 ms: 1.37x faster                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmark hidden because not significant (2): pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.57 ms: 1.62x faster                                             |
| python_startup_no_site | 5.76 ms                                                | 6.11 ms: 1.06x slower                                             |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                             |
| genshi_xml      | 63.6 ms                                                | 47.6 ms: 1.33x faster                                             |
| mako            | 14.3 ms                                                | 9.60 ms: 1.49x faster                                             |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 259 ms: 1.28x faster                                              |
| async_generators        | 428 ms                                                 | 359 ms: 1.19x faster                                              |
| async_tree_none         | 713 ms                                                 | 527 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                            |
| async_tree_memoization  | 854 ms                                                 | 668 ms: 1.28x faster                                              |
| chameleon               | 8.86 ms                                                | 6.33 ms: 1.40x faster                                             |
| chaos                   | 104 ms                                                 | 69.0 ms: 1.51x faster                                             |
| bench_thread_pool       | 943 us                                                 | 794 us: 1.19x faster                                              |
| coroutines              | 31.7 ms                                                | 25.8 ms: 1.23x faster                                             |
| coverage                | 75.3 ms                                                | 97.7 ms: 1.30x slower                                             |
| crypto_pyaes            | 118 ms                                                 | 76.8 ms: 1.53x faster                                             |
| deepcopy                | 429 us                                                 | 343 us: 1.25x faster                                              |
| deepcopy_reduce         | 3.75 us                                                | 3.05 us: 1.23x faster                                             |
| deepcopy_memo           | 50.0 us                                                | 35.6 us: 1.40x faster                                             |
| deltablue               | 7.39 ms                                                | 3.39 ms: 2.18x faster                                             |
| django_template         | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| docutils                | 3.18 sec                                               | 2.62 sec: 1.21x faster                                            |
| dulwich_log             | 75.5 ms                                                | 63.5 ms: 1.19x faster                                             |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                              |
| float                   | 108 ms                                                 | 74.1 ms: 1.45x faster                                             |
| generators              | 75.8 ms                                                | 76.1 ms: 1.00x slower                                             |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                             |
| genshi_xml              | 63.6 ms                                                | 47.6 ms: 1.33x faster                                             |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                              |
| hexiom                  | 9.42 ms                                                | 6.31 ms: 1.49x faster                                             |
| html5lib                | 85.8 ms                                                | 61.5 ms: 1.39x faster                                             |
| json                    | 5.35 ms                                                | 4.65 ms: 1.15x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| json_loads              | 28.9 us                                                | 24.1 us: 1.20x faster                                             |
| logging_format          | 8.92 us                                                | 6.51 us: 1.37x faster                                             |
| logging_silent          | 173 ns                                                 | 99.3 ns: 1.74x faster                                             |
| logging_simple          | 8.06 us                                                | 5.89 us: 1.37x faster                                             |
| mako                    | 14.3 ms                                                | 9.60 ms: 1.49x faster                                             |
| mdp                     | 2.82 sec                                               | 2.59 sec: 1.09x faster                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                              |
| mypy                    | 1.01 sec                                               | 861 ms: 1.18x faster                                              |
| nbody                   | 136 ms                                                 | 96.2 ms: 1.42x faster                                             |
| nqueens                 | 99.3 ms                                                | 79.3 ms: 1.25x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                             |
| pickle_dict             | 28.3 us                                                | 31.1 us: 1.10x slower                                             |
| pickle_list             | 4.50 us                                                | 4.07 us: 1.10x faster                                             |
| pickle_pure_python      | 453 us                                                 | 297 us: 1.53x faster                                              |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| pprint_safe_repr        | 943 ms                                                 | 689 ms: 1.37x faster                                              |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                            |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.30x faster                                            |
| pyflate                 | 675 ms                                                 | 402 ms: 1.68x faster                                              |
| python_startup          | 13.9 ms                                                | 8.57 ms: 1.62x faster                                             |
| python_startup_no_site  | 5.76 ms                                                | 6.11 ms: 1.06x slower                                             |
| raytrace                | 461 ms                                                 | 298 ms: 1.55x faster                                              |
| regex_compile           | 174 ms                                                 | 134 ms: 1.30x faster                                              |
| regex_dna               | 214 ms                                                 | 217 ms: 1.01x slower                                              |
| regex_effbot            | 3.21 ms                                                | 3.63 ms: 1.13x slower                                             |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.12x faster                                             |
| richards                | 71.4 ms                                                | 44.3 ms: 1.61x faster                                             |
| scimark_fft             | 414 ms                                                 | 311 ms: 1.33x faster                                              |
| scimark_lu              | 158 ms                                                 | 111 ms: 1.42x faster                                              |
| scimark_monte_carlo     | 105 ms                                                 | 65.1 ms: 1.61x faster                                             |
| scimark_sor             | 193 ms                                                 | 110 ms: 1.75x faster                                              |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.15 ms: 1.32x faster                                             |
| spectral_norm           | 148 ms                                                 | 98.1 ms: 1.51x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.47 ms: 1.38x faster                                             |
| sqlglot_transpile       | 2.42 ms                                                | 1.77 ms: 1.36x faster                                             |
| sqlglot_optimize        | 65.3 ms                                                | 52.7 ms: 1.24x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                             |
| sympy_expand            | 537 ms                                                 | 473 ms: 1.13x faster                                              |
| sympy_integrate         | 23.9 ms                                                | 22.1 ms: 1.08x faster                                             |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                              |
| sympy_str               | 324 ms                                                 | 291 ms: 1.12x faster                                              |
| telco                   | 6.68 ms                                                | 6.28 ms: 1.06x faster                                             |
| thrift                  | 1.03 ms                                                | 745 us: 1.38x faster                                              |
| unpack_sequence         | 59.5 ns                                                | 44.5 ns: 1.34x faster                                             |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                             |
| unpickle_pure_python    | 297 us                                                 | 203 us: 1.46x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.08x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 78.4 ms: 1.19x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 54.5 ms: 1.37x faster                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (3): bench_mp_pool, pickle, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-80ea135/bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
