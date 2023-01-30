
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 259 ms: 1.28x faster                                               |
| chameleon      | 8.86 ms                                                | 6.47 ms: 1.37x faster                                              |
| docutils       | 3.18 sec                                               | 2.61 sec: 1.22x faster                                             |
| html5lib       | 85.8 ms                                                | 60.7 ms: 1.41x faster                                              |
| Geometric mean | (ref)                                                  | 1.32x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 108 ms                                                 | 74.9 ms: 1.44x faster                                              |
| nbody          | 136 ms                                                 | 96.2 ms: 1.42x faster                                              |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                  | 1.25x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 134 ms: 1.30x faster                                               |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.10x faster                                              |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                               |
| regex_effbot   | 3.21 ms                                                | 3.47 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 299 us: 1.52x faster                                               |
| unpickle_pure_python | 297 us                                                 | 205 us: 1.45x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 54.9 ms: 1.36x faster                                              |
| json_loads           | 28.9 us                                                | 24.2 us: 1.20x faster                                              |
| xml_etree_generate   | 93.3 ms                                                | 78.8 ms: 1.18x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| pickle_list          | 4.50 us                                                | 4.17 us: 1.08x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                               |
| unpickle             | 14.3 us                                                | 13.5 us: 1.06x faster                                              |
| unpickle_list        | 4.99 us                                                | 4.88 us: 1.02x faster                                              |
| pickle               | 10.1 us                                                | 10.1 us: 1.01x faster                                              |
| pickle_dict          | 28.3 us                                                | 30.7 us: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.60 ms: 1.62x faster                                              |
| python_startup_no_site | 5.76 ms                                                | 6.13 ms: 1.06x slower                                              |
| Geometric mean         | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| mako            | 14.3 ms                                                | 9.85 ms: 1.45x faster                                              |
| django_template | 46.3 ms                                                | 34.5 ms: 1.34x faster                                              |
| genshi_xml      | 63.6 ms                                                | 47.8 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.42 ms: 2.16x faster                                              |
| logging_silent          | 173 ns                                                 | 98.6 ns: 1.76x faster                                              |
| scimark_sor             | 193 ms                                                 | 111 ms: 1.74x faster                                               |
| pyflate                 | 675 ms                                                 | 409 ms: 1.65x faster                                               |
| python_startup          | 13.9 ms                                                | 8.60 ms: 1.62x faster                                              |
| richards                | 71.4 ms                                                | 44.4 ms: 1.61x faster                                              |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 66.1 ms: 1.58x faster                                              |
| crypto_pyaes            | 118 ms                                                 | 75.9 ms: 1.55x faster                                              |
| raytrace                | 461 ms                                                 | 301 ms: 1.53x faster                                               |
| pickle_pure_python      | 453 us                                                 | 299 us: 1.52x faster                                               |
| chaos                   | 104 ms                                                 | 69.0 ms: 1.51x faster                                              |
| hexiom                  | 9.42 ms                                                | 6.31 ms: 1.49x faster                                              |
| spectral_norm           | 148 ms                                                 | 100 ms: 1.48x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.8 ms: 1.47x faster                                              |
| mako                    | 14.3 ms                                                | 9.85 ms: 1.45x faster                                              |
| unpickle_pure_python    | 297 us                                                 | 205 us: 1.45x faster                                               |
| float                   | 108 ms                                                 | 74.9 ms: 1.44x faster                                              |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.43x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 41.7 ns: 1.43x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                              |
| nbody                   | 136 ms                                                 | 96.2 ms: 1.42x faster                                              |
| html5lib                | 85.8 ms                                                | 60.7 ms: 1.41x faster                                              |
| deepcopy_memo           | 50.0 us                                                | 35.8 us: 1.39x faster                                              |
| pprint_pformat          | 1.97 sec                                               | 1.43 sec: 1.38x faster                                             |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                              |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                               |
| chameleon               | 8.86 ms                                                | 6.47 ms: 1.37x faster                                              |
| logging_format          | 8.92 us                                                | 6.57 us: 1.36x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.78 ms: 1.36x faster                                              |
| xml_etree_process       | 74.5 ms                                                | 54.9 ms: 1.36x faster                                              |
| pprint_safe_repr        | 943 ms                                                 | 697 ms: 1.35x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.07 ms: 1.35x faster                                              |
| django_template         | 46.3 ms                                                | 34.5 ms: 1.34x faster                                              |
| logging_simple          | 8.06 us                                                | 6.01 us: 1.34x faster                                              |
| async_tree_none         | 713 ms                                                 | 534 ms: 1.34x faster                                               |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                             |
| genshi_xml              | 63.6 ms                                                | 47.8 ms: 1.33x faster                                              |
| scimark_fft             | 414 ms                                                 | 315 ms: 1.31x faster                                               |
| pycparser               | 1.51 sec                                               | 1.15 sec: 1.31x faster                                             |
| fannkuch                | 477 ms                                                 | 366 ms: 1.30x faster                                               |
| regex_compile           | 174 ms                                                 | 134 ms: 1.30x faster                                               |
| 2to3                    | 332 ms                                                 | 259 ms: 1.28x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 667 ms: 1.28x faster                                               |
| nqueens                 | 99.3 ms                                                | 78.9 ms: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 765 ms: 1.24x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 109 ms: 1.24x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 53.0 ms: 1.23x faster                                              |
| deepcopy                | 429 us                                                 | 350 us: 1.23x faster                                               |
| coroutines              | 31.7 ms                                                | 26.0 ms: 1.22x faster                                              |
| docutils                | 3.18 sec                                               | 2.61 sec: 1.22x faster                                             |
| deepcopy_reduce         | 3.75 us                                                | 3.12 us: 1.20x faster                                              |
| async_generators        | 428 ms                                                 | 356 ms: 1.20x faster                                               |
| json_loads              | 28.9 us                                                | 24.2 us: 1.20x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 78.8 ms: 1.18x faster                                              |
| mypy                    | 1.01 sec                                               | 857 ms: 1.18x faster                                               |
| bench_thread_pool       | 943 us                                                 | 801 us: 1.18x faster                                               |
| dulwich_log             | 75.5 ms                                                | 64.3 ms: 1.17x faster                                              |
| sympy_expand            | 537 ms                                                 | 470 ms: 1.14x faster                                               |
| json                    | 5.35 ms                                                | 4.74 ms: 1.13x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.59 us: 1.12x faster                                              |
| sympy_str               | 324 ms                                                 | 291 ms: 1.12x faster                                               |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.10x faster                                              |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.10x faster                                               |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 22.1 ms: 1.08x faster                                              |
| pickle_list             | 4.50 us                                                | 4.17 us: 1.08x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                               |
| unpickle                | 14.3 us                                                | 13.5 us: 1.06x faster                                              |
| telco                   | 6.68 ms                                                | 6.41 ms: 1.04x faster                                              |
| unpickle_list           | 4.99 us                                                | 4.88 us: 1.02x faster                                              |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                               |
| pickle                  | 10.1 us                                                | 10.1 us: 1.01x faster                                              |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                               |
| generators              | 75.8 ms                                                | 79.9 ms: 1.05x slower                                              |
| python_startup_no_site  | 5.76 ms                                                | 6.13 ms: 1.06x slower                                              |
| regex_effbot            | 3.21 ms                                                | 3.47 ms: 1.08x slower                                              |
| pickle_dict             | 28.3 us                                                | 30.7 us: 1.08x slower                                              |
| coverage                | 75.3 ms                                                | 101 ms: 1.34x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
