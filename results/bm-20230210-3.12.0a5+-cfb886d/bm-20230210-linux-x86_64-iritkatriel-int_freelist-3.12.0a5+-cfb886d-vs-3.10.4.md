
# Results vs. 3.10.4

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.29x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| chameleon      | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| docutils       | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| html5lib       | 85.8 ms                                                | 60.5 ms: 1.42x faster                                               |
| tornado_http   | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| Geometric mean | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 108 ms                                                 | 71.9 ms: 1.50x faster                                               |
| nbody          | 136 ms                                                 | 95.4 ms: 1.43x faster                                               |
| pidigits       | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 174 ms                                                 | 127 ms: 1.37x faster                                                |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| regex_dna      | 214 ms                                                 | 219 ms: 1.02x slower                                                |
| regex_effbot   | 3.21 ms                                                | 3.43 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 453 us                                                 | 287 us: 1.58x faster                                                |
| unpickle_pure_python | 297 us                                                 | 197 us: 1.51x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.57 ms: 1.41x faster                                               |
| xml_etree_process    | 74.5 ms                                                | 55.7 ms: 1.34x faster                                               |
| json_loads           | 28.9 us                                                | 23.8 us: 1.21x faster                                               |
| xml_etree_generate   | 93.3 ms                                                | 80.8 ms: 1.16x faster                                               |
| pickle_list          | 4.50 us                                                | 4.09 us: 1.10x faster                                               |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| unpickle             | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| xml_etree_iterparse  | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| unpickle_list        | 4.99 us                                                | 4.87 us: 1.03x faster                                               |
| pickle_dict          | 28.3 us                                                | 30.9 us: 1.09x slower                                               |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| python_startup_no_site | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| mako            | 14.3 ms                                                | 9.81 ms: 1.45x faster                                               |
| django_template | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| genshi_xml      | 63.6 ms                                                | 46.9 ms: 1.36x faster                                               |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| deltablue               | 7.39 ms                                                | 3.20 ms: 2.31x faster                                               |
| logging_silent          | 173 ns                                                 | 92.4 ns: 1.87x faster                                               |
| scimark_sor             | 193 ms                                                 | 105 ms: 1.84x faster                                                |
| pyflate                 | 675 ms                                                 | 395 ms: 1.71x faster                                                |
| go                      | 226 ms                                                 | 135 ms: 1.68x faster                                                |
| raytrace                | 461 ms                                                 | 281 ms: 1.64x faster                                                |
| richards                | 71.4 ms                                                | 43.6 ms: 1.64x faster                                               |
| scimark_monte_carlo     | 105 ms                                                 | 66.2 ms: 1.58x faster                                               |
| hexiom                  | 9.42 ms                                                | 5.96 ms: 1.58x faster                                               |
| chaos                   | 104 ms                                                 | 65.9 ms: 1.58x faster                                               |
| pickle_pure_python      | 453 us                                                 | 287 us: 1.58x faster                                                |
| python_startup          | 13.9 ms                                                | 8.92 ms: 1.56x faster                                               |
| crypto_pyaes            | 118 ms                                                 | 76.5 ms: 1.54x faster                                               |
| unpickle_pure_python    | 297 us                                                 | 197 us: 1.51x faster                                                |
| spectral_norm           | 148 ms                                                 | 98.6 ms: 1.50x faster                                               |
| float                   | 108 ms                                                 | 71.9 ms: 1.50x faster                                               |
| genshi_text             | 30.6 ms                                                | 20.6 ms: 1.49x faster                                               |
| mako                    | 14.3 ms                                                | 9.81 ms: 1.45x faster                                               |
| deepcopy_memo           | 50.0 us                                                | 34.5 us: 1.45x faster                                               |
| sqlglot_parse           | 2.04 ms                                                | 1.41 ms: 1.44x faster                                               |
| scimark_lu              | 158 ms                                                 | 110 ms: 1.43x faster                                                |
| nbody                   | 136 ms                                                 | 95.4 ms: 1.43x faster                                               |
| pprint_pformat          | 1.97 sec                                               | 1.39 sec: 1.42x faster                                              |
| html5lib                | 85.8 ms                                                | 60.5 ms: 1.42x faster                                               |
| sqlglot_transpile       | 2.42 ms                                                | 1.71 ms: 1.41x faster                                               |
| chameleon               | 8.86 ms                                                | 6.28 ms: 1.41x faster                                               |
| json_dumps              | 13.5 ms                                                | 9.57 ms: 1.41x faster                                               |
| django_template         | 46.3 ms                                                | 33.1 ms: 1.40x faster                                               |
| logging_simple          | 8.06 us                                                | 5.77 us: 1.40x faster                                               |
| logging_format          | 8.92 us                                                | 6.41 us: 1.39x faster                                               |
| pprint_safe_repr        | 943 ms                                                 | 681 ms: 1.38x faster                                                |
| unpack_sequence         | 59.5 ns                                                | 43.3 ns: 1.37x faster                                               |
| scimark_fft             | 414 ms                                                 | 303 ms: 1.37x faster                                                |
| regex_compile           | 174 ms                                                 | 127 ms: 1.37x faster                                                |
| scimark_sparse_mat_mult | 5.48 ms                                                | 4.02 ms: 1.36x faster                                               |
| tornado_http            | 128 ms                                                 | 94.2 ms: 1.36x faster                                               |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                |
| genshi_xml              | 63.6 ms                                                | 46.9 ms: 1.36x faster                                               |
| async_tree_none         | 713 ms                                                 | 526 ms: 1.35x faster                                                |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                              |
| pycparser               | 1.51 sec                                               | 1.13 sec: 1.34x faster                                              |
| aiohttp                 | 1.34 ms                                                | 1.00 ms: 1.34x faster                                               |
| xml_etree_process       | 74.5 ms                                                | 55.7 ms: 1.34x faster                                               |
| gunicorn                | 1.43 ms                                                | 1.08 ms: 1.33x faster                                               |
| 2to3                    | 332 ms                                                 | 252 ms: 1.32x faster                                                |
| deepcopy                | 429 us                                                 | 330 us: 1.30x faster                                                |
| async_tree_memoization  | 854 ms                                                 | 659 ms: 1.30x faster                                                |
| fannkuch                | 477 ms                                                 | 368 ms: 1.30x faster                                                |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                |
| sqlglot_optimize        | 65.3 ms                                                | 51.1 ms: 1.28x faster                                               |
| deepcopy_reduce         | 3.75 us                                                | 2.93 us: 1.28x faster                                               |
| docutils                | 3.18 sec                                               | 2.52 sec: 1.26x faster                                              |
| async_tree_cpu_io_mixed | 949 ms                                                 | 755 ms: 1.26x faster                                                |
| nqueens                 | 99.3 ms                                                | 79.1 ms: 1.26x faster                                               |
| coroutines              | 31.7 ms                                                | 25.6 ms: 1.24x faster                                               |
| json_loads              | 28.9 us                                                | 23.8 us: 1.21x faster                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                                |
| dulwich_log             | 75.5 ms                                                | 62.3 ms: 1.21x faster                                               |
| sympy_integrate         | 23.9 ms                                                | 19.8 ms: 1.21x faster                                               |
| bench_thread_pool       | 943 us                                                 | 782 us: 1.21x faster                                                |
| sympy_str               | 324 ms                                                 | 270 ms: 1.20x faster                                                |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.19x faster                                               |
| sympy_expand            | 537 ms                                                 | 457 ms: 1.17x faster                                                |
| sqlalchemy_imperative   | 21.0 ms                                                | 18.0 ms: 1.17x faster                                               |
| sympy_sum               | 183 ms                                                 | 157 ms: 1.16x faster                                                |
| mdp                     | 2.82 sec                                               | 2.44 sec: 1.16x faster                                              |
| xml_etree_generate      | 93.3 ms                                                | 80.8 ms: 1.16x faster                                               |
| json                    | 5.35 ms                                                | 4.67 ms: 1.15x faster                                               |
| sqlite_synth            | 2.90 us                                                | 2.58 us: 1.13x faster                                               |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                               |
| pickle_list             | 4.50 us                                                | 4.09 us: 1.10x faster                                               |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                |
| unpickle                | 14.3 us                                                | 13.2 us: 1.08x faster                                               |
| xml_etree_iterparse     | 110 ms                                                 | 103 ms: 1.07x faster                                                |
| telco                   | 6.68 ms                                                | 6.42 ms: 1.04x faster                                               |
| unpickle_list           | 4.99 us                                                | 4.87 us: 1.03x faster                                               |
| generators              | 75.8 ms                                                | 75.4 ms: 1.01x faster                                               |
| regex_dna               | 214 ms                                                 | 219 ms: 1.02x slower                                                |
| pidigits                | 190 ms                                                 | 203 ms: 1.07x slower                                                |
| regex_effbot            | 3.21 ms                                                | 3.43 ms: 1.07x slower                                               |
| pickle_dict             | 28.3 us                                                | 30.9 us: 1.09x slower                                               |
| python_startup_no_site  | 5.76 ms                                                | 6.48 ms: 1.12x slower                                               |
| coverage                | 75.3 ms                                                | 95.9 ms: 1.27x slower                                               |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (3): pickle, bench_mp_pool, async_generators
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230210-3.12.0a5+-cfb886d/bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
