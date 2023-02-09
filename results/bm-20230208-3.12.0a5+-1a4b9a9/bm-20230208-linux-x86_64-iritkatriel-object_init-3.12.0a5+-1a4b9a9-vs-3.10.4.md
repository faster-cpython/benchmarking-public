
# Results vs. 3.10.4

- fork: iritkatriel
- ref: object_init
- machine: linux-x86_64
- commit hash: 1a4b9a9
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 251 ms: 1.33x faster                                               |
| chameleon      | 8.86 ms                                                | 6.36 ms: 1.39x faster                                              |
| docutils       | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| html5lib       | 85.8 ms                                                | 60.9 ms: 1.41x faster                                              |
| tornado_http   | 128 ms                                                 | 94.0 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 136 ms                                                 | 86.0 ms: 1.58x faster                                              |
| float          | 108 ms                                                 | 72.1 ms: 1.50x faster                                              |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 128 ms: 1.36x faster                                               |
| regex_v8       | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| regex_dna      | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| regex_effbot   | 3.21 ms                                                | 3.32 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 288 us: 1.57x faster                                               |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.50x faster                                               |
| json_dumps           | 13.5 ms                                                | 9.34 ms: 1.44x faster                                              |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                              |
| json_loads           | 28.9 us                                                | 23.7 us: 1.22x faster                                              |
| xml_etree_generate   | 93.3 ms                                                | 81.3 ms: 1.15x faster                                              |
| pickle_list          | 4.50 us                                                | 4.09 us: 1.10x faster                                              |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle             | 14.3 us                                                | 13.1 us: 1.09x faster                                              |
| xml_etree_iterparse  | 110 ms                                                 | 108 ms: 1.02x faster                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                              |
| pickle_dict          | 28.3 us                                                | 30.6 us: 1.08x slower                                              |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.97 ms: 1.55x faster                                              |
| python_startup_no_site | 5.76 ms                                                | 6.51 ms: 1.13x slower                                              |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.3 ms                                                | 9.65 ms: 1.48x faster                                              |
| genshi_text     | 30.6 ms                                                | 20.7 ms: 1.48x faster                                              |
| django_template | 46.3 ms                                                | 32.4 ms: 1.43x faster                                              |
| genshi_xml      | 63.6 ms                                                | 46.4 ms: 1.37x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.18 ms: 2.33x faster                                              |
| logging_silent          | 173 ns                                                 | 92.3 ns: 1.88x faster                                              |
| scimark_sor             | 193 ms                                                 | 108 ms: 1.80x faster                                               |
| richards                | 71.4 ms                                                | 42.2 ms: 1.69x faster                                              |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                               |
| pyflate                 | 675 ms                                                 | 403 ms: 1.68x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 71.3 ms: 1.65x faster                                              |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                               |
| chaos                   | 104 ms                                                 | 64.1 ms: 1.62x faster                                              |
| scimark_monte_carlo     | 105 ms                                                 | 65.0 ms: 1.61x faster                                              |
| nbody                   | 136 ms                                                 | 86.0 ms: 1.58x faster                                              |
| hexiom                  | 9.42 ms                                                | 5.95 ms: 1.58x faster                                              |
| pickle_pure_python      | 453 us                                                 | 288 us: 1.57x faster                                               |
| python_startup          | 13.9 ms                                                | 8.97 ms: 1.55x faster                                              |
| spectral_norm           | 148 ms                                                 | 95.9 ms: 1.54x faster                                              |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.50x faster                                               |
| float                   | 108 ms                                                 | 72.1 ms: 1.50x faster                                              |
| scimark_lu              | 158 ms                                                 | 106 ms: 1.49x faster                                               |
| mako                    | 14.3 ms                                                | 9.65 ms: 1.48x faster                                              |
| genshi_text             | 30.6 ms                                                | 20.7 ms: 1.48x faster                                              |
| deepcopy_memo           | 50.0 us                                                | 33.9 us: 1.48x faster                                              |
| json_dumps              | 13.5 ms                                                | 9.34 ms: 1.44x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                              |
| django_template         | 46.3 ms                                                | 32.4 ms: 1.43x faster                                              |
| pprint_pformat          | 1.97 sec                                               | 1.40 sec: 1.41x faster                                             |
| html5lib                | 85.8 ms                                                | 60.9 ms: 1.41x faster                                              |
| logging_format          | 8.92 us                                                | 6.34 us: 1.41x faster                                              |
| sqlglot_transpile       | 2.42 ms                                                | 1.72 ms: 1.41x faster                                              |
| scimark_sparse_mat_mult | 5.48 ms                                                | 3.90 ms: 1.41x faster                                              |
| unpack_sequence         | 59.5 ns                                                | 42.6 ns: 1.39x faster                                              |
| chameleon               | 8.86 ms                                                | 6.36 ms: 1.39x faster                                              |
| logging_simple          | 8.06 us                                                | 5.79 us: 1.39x faster                                              |
| scimark_fft             | 414 ms                                                 | 298 ms: 1.39x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 680 ms: 1.39x faster                                               |
| pycparser               | 1.51 sec                                               | 1.10 sec: 1.38x faster                                             |
| genshi_xml              | 63.6 ms                                                | 46.4 ms: 1.37x faster                                              |
| tornado_http            | 128 ms                                                 | 94.0 ms: 1.36x faster                                              |
| async_tree_io           | 1.78 sec                                               | 1.30 sec: 1.36x faster                                             |
| async_tree_none         | 713 ms                                                 | 523 ms: 1.36x faster                                               |
| regex_compile           | 174 ms                                                 | 128 ms: 1.36x faster                                               |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                               |
| async_tree_memoization  | 854 ms                                                 | 635 ms: 1.34x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.33x faster                                              |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                              |
| 2to3                    | 332 ms                                                 | 251 ms: 1.33x faster                                               |
| deepcopy                | 429 us                                                 | 328 us: 1.31x faster                                               |
| fannkuch                | 477 ms                                                 | 369 ms: 1.29x faster                                               |
| coroutines              | 31.7 ms                                                | 24.5 ms: 1.29x faster                                              |
| deepcopy_reduce         | 3.75 us                                                | 2.92 us: 1.29x faster                                              |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.28x faster                                               |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 752 ms: 1.26x faster                                               |
| nqueens                 | 99.3 ms                                                | 78.8 ms: 1.26x faster                                              |
| docutils                | 3.18 sec                                               | 2.56 sec: 1.24x faster                                             |
| json_loads              | 28.9 us                                                | 23.7 us: 1.22x faster                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                              |
| bench_thread_pool       | 943 us                                                 | 786 us: 1.20x faster                                               |
| sympy_str               | 324 ms                                                 | 271 ms: 1.20x faster                                               |
| dulwich_log             | 75.5 ms                                                | 63.1 ms: 1.20x faster                                              |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.18x faster                                               |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.0 ms: 1.17x faster                                              |
| regex_v8                | 25.0 ms                                                | 21.4 ms: 1.17x faster                                              |
| sympy_sum               | 183 ms                                                 | 158 ms: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.64 ms: 1.15x faster                                              |
| mdp                     | 2.82 sec                                               | 2.45 sec: 1.15x faster                                             |
| xml_etree_generate      | 93.3 ms                                                | 81.3 ms: 1.15x faster                                              |
| sqlite_synth            | 2.90 us                                                | 2.56 us: 1.13x faster                                              |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.13x faster                                              |
| pickle_list             | 4.50 us                                                | 4.09 us: 1.10x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                               |
| unpickle                | 14.3 us                                                | 13.1 us: 1.09x faster                                              |
| meteor_contest          | 114 ms                                                 | 107 ms: 1.06x faster                                               |
| telco                   | 6.68 ms                                                | 6.40 ms: 1.04x faster                                              |
| xml_etree_iterparse     | 110 ms                                                 | 108 ms: 1.02x faster                                               |
| regex_dna               | 214 ms                                                 | 211 ms: 1.01x faster                                               |
| async_generators        | 428 ms                                                 | 423 ms: 1.01x faster                                               |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                               |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                              |
| generators              | 75.8 ms                                                | 76.5 ms: 1.01x slower                                              |
| regex_effbot            | 3.21 ms                                                | 3.32 ms: 1.03x slower                                              |
| pickle_dict             | 28.3 us                                                | 30.6 us: 1.08x slower                                              |
| python_startup_no_site  | 5.76 ms                                                | 6.51 ms: 1.13x slower                                              |
| coverage                | 75.3 ms                                                | 97.3 ms: 1.29x slower                                              |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                       |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230208-3.12.0a5+-1a4b9a9/bm-20230208-linux-x86_64-iritkatriel-object_init-3.12.0a5+-1a4b9a9.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
