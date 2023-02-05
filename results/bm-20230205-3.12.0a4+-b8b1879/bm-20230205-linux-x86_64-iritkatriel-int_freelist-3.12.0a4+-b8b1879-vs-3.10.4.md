
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: b8b1879
- commit date: 2023-02-05
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.34 ms: 1.40x faster                                               |
| docutils       | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| html5lib       | 85.8 ms                                                | 60.2 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 94.3 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 72.9 ms: 1.48x faster                                               |
| nbody          | 136 ms                                                 | 99.5 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 129 ms: 1.35x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.11x faster                                               |
| regex_dna      | 214 ms                                                 | 214 ms: 1.00x slower                                                |
| regex_effbot   | 3.21 ms                                                | 3.62 ms: 1.13x slower                                               |
| Geometric mean | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 198 us: 1.49x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.51 ms: 1.42x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 53.7 ms: 1.39x faster                                               |
| json_loads           | 28.9 us                                                | 23.5 us: 1.23x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 78.1 ms: 1.19x faster                                               |
| pickle_list          | 4.50 us                                                | 4.00 us: 1.13x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.84 us: 1.03x faster                                               |
| pickle               | 10.1 us                                                | 9.98 us: 1.02x faster                                               |
| pickle_dict          | 28.3 us                                                | 30.1 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.46 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.62 ms: 1.48x faster                                               |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.45x faster                                               |
| django_template | 46.3 ms                                                | 32.5 ms: 1.42x faster                                               |
| genshi_xml      | 63.6 ms                                                | 47.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.21 ms: 2.30x faster                                               |
| logging_silent          | 173 ns                                                 | 92.6 ns: 1.87x faster                                               |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                                |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                                |
| richards                | 71.4 ms                                                | 42.4 ms: 1.68x faster                                               |
| pyflate                 | 675 ms                                                 | 401 ms: 1.68x faster                                                |
| chaos                   | 104 ms                                                 | 63.2 ms: 1.65x faster                                               |
| raytrace                | 461 ms                                                 | 287 ms: 1.61x faster                                                |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                |
| hexiom                  | 9.42 ms                                                | 5.98 ms: 1.57x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 75.2 ms: 1.56x faster                                               |
| python_startup          | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| spectral_norm           | 148 ms                                                 | 95.0 ms: 1.56x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 67.7 ms: 1.55x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 198 us: 1.49x faster                                                |
| mako                    | 14.3 ms                                                | 9.62 ms: 1.48x faster                                               |
| float                   | 108 ms                                                 | 72.9 ms: 1.48x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.45x faster                                               |
| scimark_lu              | 158 ms                                                 | 109 ms: 1.45x faster                                                |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.45x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.7 us: 1.44x faster                                               |
| html5lib                | 85.8 ms                                                | 60.2 ms: 1.42x faster                                               |
| django_template         | 46.3 ms                                                | 32.5 ms: 1.42x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.70 ms: 1.42x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.51 ms: 1.42x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.41 sec: 1.40x faster                                              |
| logging_format          | 8.92 us                                                | 6.38 us: 1.40x faster                                               |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.92 ms: 1.40x faster                                               |
| logging_simple          | 8.06 us                                                | 5.76 us: 1.40x faster                                               |
| chameleon               | 8.86 ms                                                | 6.34 ms: 1.40x faster                                               |
| thrift                  | 1.03 ms                                                | 741 us: 1.39x faster                                                |
| xml_etree_process       | 74.5 ms                                                | 53.7 ms: 1.39x faster                                               |
| unpack_sequence         | 59.5 ns                                                | 43.2 ns: 1.38x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 686 ms: 1.37x faster                                                |
| nbody                   | 136 ms                                                 | 99.5 ms: 1.37x faster                                               |
| tornado_http            | 128 ms                                                 | 94.3 ms: 1.36x faster                                               |
| async_tree_none         | 713 ms                                                 | 527 ms: 1.35x faster                                                |
| regex_compile           | 174 ms                                                 | 129 ms: 1.35x faster                                                |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.34x faster                                              |
| scimark_fft             | 414 ms                                                 | 309 ms: 1.34x faster                                                |
| aiohttp                 | 1.34 ms                                                | 999 us: 1.34x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.34x faster                                              |
| genshi_xml              | 63.6 ms                                                | 47.7 ms: 1.33x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| fannkuch                | 477 ms                                                 | 367 ms: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| nqueens                 | 99.3 ms                                                | 77.0 ms: 1.29x faster                                               |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                |
| deepcopy                | 429 us                                                 | 336 us: 1.28x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                               |
| coroutines              | 31.7 ms                                                | 24.9 ms: 1.27x faster                                               |
| docutils                | 3.18 sec                                               | 2.50 sec: 1.27x faster                                              |
| mypy                    | 1.01 sec                                               | 805 ms: 1.26x faster                                                |
| deepcopy_reduce         | 3.75 us                                                | 3.01 us: 1.25x faster                                               |
| async_tree_cpu_io_mixed | 949 ms                                                 | 762 ms: 1.25x faster                                                |
| json_loads              | 28.9 us                                                | 23.5 us: 1.23x faster                                               |
| async_generators        | 428 ms                                                 | 349 ms: 1.22x faster                                                |
| dulwich_log             | 75.5 ms                                                | 62.4 ms: 1.21x faster                                               |
| bench_thread_pool       | 943 us                                                 | 780 us: 1.21x faster                                                |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| xml_etree_generate      | 93.3 ms                                                | 78.1 ms: 1.19x faster                                               |
| sympy_str               | 324 ms                                                 | 272 ms: 1.19x faster                                                |
| json                    | 5.35 ms                                                | 4.55 ms: 1.18x faster                                               |
| sympy_sum               | 183 ms                                                 | 156 ms: 1.18x faster                                                |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlite_synth            | 2.90 us                                                | 2.55 us: 1.14x faster                                               |
| mdp                     | 2.82 sec                                               | 2.49 sec: 1.13x faster                                              |
| pickle_list             | 4.50 us                                                | 4.00 us: 1.13x faster                                               |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.11x faster                                               |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| xml_etree_iterparse     | 110 ms                                                 | 102 ms: 1.08x faster                                                |
| telco                   | 6.68 ms                                                | 6.42 ms: 1.04x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.84 us: 1.03x faster                                               |
| pickle                  | 10.1 us                                                | 9.98 us: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 214 ms: 1.00x slower                                                |
| generators              | 75.8 ms                                                | 76.8 ms: 1.01x slower                                               |
| pickle_dict             | 28.3 us                                                | 30.1 us: 1.06x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.46 ms: 1.12x slower                                               |
| regex_effbot            | 3.21 ms                                                | 3.62 ms: 1.13x slower                                               |
| coverage                | 75.3 ms                                                | 98.9 ms: 1.31x slower                                               |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                        |

Benchmark hidden because not significant (2): bench_mp_pool, pidigits
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230205-3.12.0a4+-b8b1879/bm-20230205-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-b8b1879.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
