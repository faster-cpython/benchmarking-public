
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
| chameleon      | 8.86 ms                                                | 6.50 ms: 1.36x faster                                             |
| docutils       | 3.18 sec                                               | 2.61 sec: 1.22x faster                                            |
| html5lib       | 85.8 ms                                                | 61.5 ms: 1.39x faster                                             |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 108 ms                                                 | 73.3 ms: 1.47x faster                                             |
| nbody          | 136 ms                                                 | 95.9 ms: 1.42x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.26x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 134 ms: 1.29x faster                                              |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                              |
| regex_effbot   | 3.21 ms                                                | 3.53 ms: 1.10x slower                                             |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 13.5 ms                                                | 9.45 ms: 1.43x faster                                             |
| json_loads           | 28.9 us                                                | 24.0 us: 1.21x faster                                             |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                             |
| pickle_dict          | 28.3 us                                                | 32.4 us: 1.14x slower                                             |
| pickle_list          | 4.50 us                                                | 4.37 us: 1.03x faster                                             |
| pickle_pure_python   | 453 us                                                 | 295 us: 1.54x faster                                              |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                             |
| unpickle_pure_python | 297 us                                                 | 203 us: 1.46x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 104 ms: 1.06x faster                                              |
| xml_etree_generate   | 93.3 ms                                                | 77.5 ms: 1.20x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 54.1 ms: 1.38x faster                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.58 ms: 1.62x faster                                             |
| python_startup_no_site | 5.76 ms                                                | 6.11 ms: 1.06x slower                                             |
| Geometric mean         | (ref)                                                  | 1.24x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 46.3 ms                                                | 34.0 ms: 1.36x faster                                             |
| genshi_text     | 30.6 ms                                                | 21.1 ms: 1.45x faster                                             |
| genshi_xml      | 63.6 ms                                                | 48.1 ms: 1.32x faster                                             |
| mako            | 14.3 ms                                                | 9.85 ms: 1.45x faster                                             |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3                    | 332 ms                                                 | 258 ms: 1.29x faster                                              |
| async_generators        | 428 ms                                                 | 357 ms: 1.20x faster                                              |
| async_tree_none         | 713 ms                                                 | 524 ms: 1.36x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 756 ms: 1.25x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                            |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                              |
| chameleon               | 8.86 ms                                                | 6.50 ms: 1.36x faster                                             |
| chaos                   | 104 ms                                                 | 68.9 ms: 1.51x faster                                             |
| bench_thread_pool       | 943 us                                                 | 792 us: 1.19x faster                                              |
| coroutines              | 31.7 ms                                                | 26.1 ms: 1.21x faster                                             |
| coverage                | 75.3 ms                                                | 97.5 ms: 1.29x slower                                             |
| crypto_pyaes            | 118 ms                                                 | 76.8 ms: 1.53x faster                                             |
| deepcopy                | 429 us                                                 | 346 us: 1.24x faster                                              |
| deepcopy_reduce         | 3.75 us                                                | 3.00 us: 1.25x faster                                             |
| deepcopy_memo           | 50.0 us                                                | 35.8 us: 1.40x faster                                             |
| deltablue               | 7.39 ms                                                | 3.39 ms: 2.18x faster                                             |
| django_template         | 46.3 ms                                                | 34.0 ms: 1.36x faster                                             |
| docutils                | 3.18 sec                                               | 2.61 sec: 1.22x faster                                            |
| dulwich_log             | 75.5 ms                                                | 63.6 ms: 1.19x faster                                             |
| fannkuch                | 477 ms                                                 | 379 ms: 1.26x faster                                              |
| float                   | 108 ms                                                 | 73.3 ms: 1.47x faster                                             |
| generators              | 75.8 ms                                                | 76.3 ms: 1.01x slower                                             |
| genshi_text             | 30.6 ms                                                | 21.1 ms: 1.45x faster                                             |
| genshi_xml              | 63.6 ms                                                | 48.1 ms: 1.32x faster                                             |
| go                      | 226 ms                                                 | 140 ms: 1.62x faster                                              |
| hexiom                  | 9.42 ms                                                | 6.32 ms: 1.49x faster                                             |
| html5lib                | 85.8 ms                                                | 61.5 ms: 1.39x faster                                             |
| json                    | 5.35 ms                                                | 4.71 ms: 1.14x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.45 ms: 1.43x faster                                             |
| json_loads              | 28.9 us                                                | 24.0 us: 1.21x faster                                             |
| logging_format          | 8.92 us                                                | 6.51 us: 1.37x faster                                             |
| logging_silent          | 173 ns                                                 | 98.2 ns: 1.76x faster                                             |
| logging_simple          | 8.06 us                                                | 5.90 us: 1.36x faster                                             |
| mako                    | 14.3 ms                                                | 9.85 ms: 1.45x faster                                             |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                            |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                              |
| mypy                    | 1.01 sec                                               | 858 ms: 1.18x faster                                              |
| nbody                   | 136 ms                                                 | 95.9 ms: 1.42x faster                                             |
| nqueens                 | 99.3 ms                                                | 83.5 ms: 1.19x faster                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                             |
| pickle_dict             | 28.3 us                                                | 32.4 us: 1.14x slower                                             |
| pickle_list             | 4.50 us                                                | 4.37 us: 1.03x faster                                             |
| pickle_pure_python      | 453 us                                                 | 295 us: 1.54x faster                                              |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| pprint_safe_repr        | 943 ms                                                 | 704 ms: 1.34x faster                                              |
| pprint_pformat          | 1.97 sec                                               | 1.42 sec: 1.39x faster                                            |
| pycparser               | 1.51 sec                                               | 1.16 sec: 1.30x faster                                            |
| pyflate                 | 675 ms                                                 | 408 ms: 1.66x faster                                              |
| python_startup          | 13.9 ms                                                | 8.58 ms: 1.62x faster                                             |
| python_startup_no_site  | 5.76 ms                                                | 6.11 ms: 1.06x slower                                             |
| raytrace                | 461 ms                                                 | 296 ms: 1.56x faster                                              |
| regex_compile           | 174 ms                                                 | 134 ms: 1.29x faster                                              |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                              |
| regex_effbot            | 3.21 ms                                                | 3.53 ms: 1.10x slower                                             |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                             |
| richards                | 71.4 ms                                                | 43.8 ms: 1.63x faster                                             |
| scimark_fft             | 414 ms                                                 | 315 ms: 1.31x faster                                              |
| scimark_lu              | 158 ms                                                 | 112 ms: 1.41x faster                                              |
| scimark_monte_carlo     | 105 ms                                                 | 64.9 ms: 1.61x faster                                             |
| scimark_sor             | 193 ms                                                 | 109 ms: 1.77x faster                                              |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.05 ms: 1.35x faster                                             |
| spectral_norm           | 148 ms                                                 | 96.4 ms: 1.54x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.45 ms: 1.41x faster                                             |
| sqlglot_transpile       | 2.42 ms                                                | 1.76 ms: 1.38x faster                                             |
| sqlglot_optimize        | 65.3 ms                                                | 52.6 ms: 1.24x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.60 us: 1.12x faster                                             |
| sympy_expand            | 537 ms                                                 | 474 ms: 1.13x faster                                              |
| sympy_integrate         | 23.9 ms                                                | 22.1 ms: 1.08x faster                                             |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                              |
| sympy_str               | 324 ms                                                 | 291 ms: 1.11x faster                                              |
| telco                   | 6.68 ms                                                | 6.38 ms: 1.05x faster                                             |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                              |
| unpack_sequence         | 59.5 ns                                                | 42.1 ns: 1.41x faster                                             |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                             |
| unpickle_pure_python    | 297 us                                                 | 203 us: 1.46x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 104 ms: 1.06x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 77.5 ms: 1.20x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 54.1 ms: 1.38x faster                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-15497c4/bm-20230117-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-15497c4.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
