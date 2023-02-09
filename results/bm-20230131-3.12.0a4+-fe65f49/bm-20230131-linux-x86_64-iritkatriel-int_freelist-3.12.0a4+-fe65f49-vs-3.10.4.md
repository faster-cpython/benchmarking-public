
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: fe65f49
- commit date: 2023-01-31
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 253 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.29 ms: 1.41x faster                                               |
| docutils       | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 61.9 ms: 1.39x faster                                               |
| tornado_http   | 128 ms                                                 | 95.0 ms: 1.35x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.8 ms: 1.48x faster                                               |
| nbody          | 136 ms                                                 | 97.9 ms: 1.39x faster                                               |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| regex_dna      | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| regex_effbot   | 3.21 ms                                                | 3.50 ms: 1.09x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 285 us: 1.59x faster                                                |
| unpickle_pure_python | 297 us                                                 | 199 us: 1.49x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.35 ms: 1.44x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 77.7 ms: 1.20x faster                                               |
| json_loads           | 28.9 us                                                | 24.6 us: 1.17x faster                                               |
| pickle_list          | 4.50 us                                                | 4.09 us: 1.10x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| unpickle             | 14.3 us                                                | 13.6 us: 1.05x faster                                               |
| unpickle_list        | 4.99 us                                                | 4.90 us: 1.02x faster                                               |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| pickle_dict          | 28.3 us                                                | 30.5 us: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.94 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.2 ms: 1.52x faster                                               |
| mako            | 14.3 ms                                                | 9.82 ms: 1.45x faster                                               |
| django_template | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.0 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.24 ms: 2.28x faster                                               |
| logging_silent          | 173 ns                                                 | 91.3 ns: 1.90x faster                                               |
| go                      | 226 ms                                                 | 138 ms: 1.64x faster                                                |
| richards                | 71.4 ms                                                | 43.8 ms: 1.63x faster                                               |
| pickle_pure_python      | 453 us                                                 | 285 us: 1.59x faster                                                |
| raytrace                | 461 ms                                                 | 292 ms: 1.58x faster                                                |
| hexiom                  | 9.42 ms                                                | 5.99 ms: 1.57x faster                                               |
| chaos                   | 104 ms                                                 | 66.4 ms: 1.57x faster                                               |
| python_startup          | 13.9 ms                                                | 8.94 ms: 1.56x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 67.6 ms: 1.55x faster                                               |
| scimark_sor             | 193 ms                                                 | 125 ms: 1.54x faster                                                |
| genshi_text             | 30.6 ms                                                | 20.2 ms: 1.52x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 199 us: 1.49x faster                                                |
| scimark_lu              | 158 ms                                                 | 107 ms: 1.48x faster                                                |
| float                   | 108 ms                                                 | 72.8 ms: 1.48x faster                                               |
| mako                    | 14.3 ms                                                | 9.82 ms: 1.45x faster                                               |
| pyflate                 | 675 ms                                                 | 467 ms: 1.45x faster                                                |
| json_dumps              | 13.5 ms                                                | 9.35 ms: 1.44x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                               |
| logging_format          | 8.92 us                                                | 6.29 us: 1.42x faster                                               |
| django_template         | 46.3 ms                                                | 32.6 ms: 1.42x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                              |
| logging_simple          | 8.06 us                                                | 5.72 us: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.29 ms: 1.41x faster                                               |
| thrift                  | 1.03 ms                                                | 735 us: 1.40x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.2 ms: 1.40x faster                                               |
| nbody                   | 136 ms                                                 | 97.9 ms: 1.39x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 678 ms: 1.39x faster                                                |
| html5lib                | 85.8 ms                                                | 61.9 ms: 1.39x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 43.0 ns: 1.38x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.48 ms: 1.38x faster                                               |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                                |
| sqlglot_transpile       | 2.42 ms                                                | 1.78 ms: 1.36x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.31 sec: 1.36x faster                                              |
| genshi_xml              | 63.6 ms                                                | 47.0 ms: 1.35x faster                                               |
| pycparser               | 1.51 sec                                               | 1.12 sec: 1.35x faster                                              |
| tornado_http            | 128 ms                                                 | 95.0 ms: 1.35x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| 2to3                    | 332 ms                                                 | 253 ms: 1.32x faster                                                |
| crypto_pyaes            | 118 ms                                                 | 89.5 ms: 1.31x faster                                               |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                |
| fannkuch                | 477 ms                                                 | 369 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.96 us: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.51 sec: 1.27x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                                |
| mypy                    | 1.01 sec                                               | 807 ms: 1.26x faster                                                |
| nqueens                 | 99.3 ms                                                | 79.3 ms: 1.25x faster                                               |
| coroutines              | 31.7 ms                                                | 25.5 ms: 1.24x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.48 ms: 1.22x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 77.7 ms: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| sympy_expand            | 537 ms                                                 | 453 ms: 1.18x faster                                                |
| sympy_sum               | 183 ms                                                 | 155 ms: 1.18x faster                                                |
| bench_thread_pool       | 943 us                                                 | 800 us: 1.18x faster                                                |
| dulwich_log             | 75.5 ms                                                | 64.3 ms: 1.17x faster                                               |
| json_loads              | 28.9 us                                                | 24.6 us: 1.17x faster                                               |
| async_generators        | 428 ms                                                 | 372 ms: 1.15x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                               |
| json                    | 5.35 ms                                                | 4.67 ms: 1.15x faster                                               |
| pickle_list             | 4.50 us                                                | 4.09 us: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.08x faster                                                |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| sqlite_synth            | 2.90 us                                                | 2.70 us: 1.07x faster                                               |
| pathlib                 | 20.0 ms                                                | 19.0 ms: 1.05x faster                                               |
| unpickle                | 14.3 us                                                | 13.6 us: 1.05x faster                                               |
| spectral_norm           | 148 ms                                                 | 141 ms: 1.05x faster                                                |
| telco                   | 6.68 ms                                                | 6.37 ms: 1.05x faster                                               |
| scimark_fft             | 414 ms                                                 | 397 ms: 1.04x faster                                                |
| mdp                     | 2.82 sec                                               | 2.72 sec: 1.04x faster                                              |
| regex_dna               | 214 ms                                                 | 210 ms: 1.02x faster                                                |
| unpickle_list           | 4.99 us                                                | 4.90 us: 1.02x faster                                               |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                               |
| generators              | 75.8 ms                                                | 81.0 ms: 1.07x slower                                               |
| pickle_dict             | 28.3 us                                                | 30.5 us: 1.08x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.50 ms: 1.09x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.47 ms: 1.12x slower                                               |
| coverage                | 75.3 ms                                                | 95.1 ms: 1.26x slower                                               |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230131-3.12.0a4+-fe65f49/bm-20230131-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-fe65f49.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
