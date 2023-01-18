
# Results vs. 3.11.0

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.25x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 333 ms: 1.29x slower                                                   |
| docutils       | 2.60 sec                                               | 3.17 sec: 1.22x slower                                                 |
| html5lib       | 63.2 ms                                                | 86.5 ms: 1.37x slower                                                  |
| tornado_http   | 96.6 ms                                                | 129 ms: 1.34x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 76.3 ms                                                | 107 ms: 1.40x slower                                                   |
| nbody          | 95.0 ms                                                | 141 ms: 1.48x slower                                                   |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.26x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 171 ms: 1.26x slower                                                   |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                   |
| regex_effbot   | 3.36 ms                                                | 3.24 ms: 1.04x faster                                                  |
| regex_v8       | 22.3 ms                                                | 25.4 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 13.7 ms: 1.08x slower                                                  |
| json_loads           | 26.2 us                                                | 28.4 us: 1.08x slower                                                  |
| pickle               | 9.79 us                                                | 10.0 us: 1.03x slower                                                  |
| pickle_dict          | 31.4 us                                                | 26.9 us: 1.17x faster                                                  |
| pickle_list          | 4.17 us                                                | 4.45 us: 1.07x slower                                                  |
| pickle_pure_python   | 304 us                                                 | 451 us: 1.48x slower                                                   |
| unpickle             | 13.3 us                                                | 14.3 us: 1.08x slower                                                  |
| unpickle_list        | 4.95 us                                                | 5.01 us: 1.01x slower                                                  |
| unpickle_pure_python | 225 us                                                 | 294 us: 1.30x slower                                                   |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 103 ms                                                 | 110 ms: 1.07x slower                                                   |
| xml_etree_generate   | 76.2 ms                                                | 92.4 ms: 1.21x slower                                                  |
| xml_etree_process    | 53.8 ms                                                | 73.2 ms: 1.36x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 15.2 ms: 1.82x slower                                                  |
| python_startup_no_site | 5.96 ms                                                | 5.79 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.33x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 32.5 ms                                                | 46.2 ms: 1.42x slower                                                  |
| genshi_text     | 22.1 ms                                                | 30.1 ms: 1.36x slower                                                  |
| genshi_xml      | 52.1 ms                                                | 63.2 ms: 1.21x slower                                                  |
| mako            | 9.85 ms                                                | 14.7 ms: 1.49x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.37x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3                    | 257 ms                                                 | 333 ms: 1.29x slower                                                   |
| async_generators        | 359 ms                                                 | 420 ms: 1.17x slower                                                   |
| async_tree_none         | 529 ms                                                 | 712 ms: 1.34x slower                                                   |
| async_tree_cpu_io_mixed | 752 ms                                                 | 977 ms: 1.30x slower                                                   |
| async_tree_io           | 1.31 sec                                               | 1.80 sec: 1.38x slower                                                 |
| async_tree_memoization  | 625 ms                                                 | 848 ms: 1.36x slower                                                   |
| chaos                   | 68.6 ms                                                | 106 ms: 1.55x slower                                                   |
| bench_thread_pool       | 810 us                                                 | 960 us: 1.19x slower                                                   |
| coroutines              | 26.1 ms                                                | 30.4 ms: 1.17x slower                                                  |
| coverage                | 101 ms                                                 | 65.8 ms: 1.53x faster                                                  |
| crypto_pyaes            | 73.9 ms                                                | 118 ms: 1.59x slower                                                   |
| deepcopy                | 344 us                                                 | 423 us: 1.23x slower                                                   |
| deepcopy_reduce         | 2.97 us                                                | 3.73 us: 1.26x slower                                                  |
| deepcopy_memo           | 36.4 us                                                | 48.8 us: 1.34x slower                                                  |
| deltablue               | 3.64 ms                                                | 7.29 ms: 2.00x slower                                                  |
| django_template         | 32.5 ms                                                | 46.2 ms: 1.42x slower                                                  |
| docutils                | 2.60 sec                                               | 3.17 sec: 1.22x slower                                                 |
| dulwich_log             | 63.9 ms                                                | 75.6 ms: 1.18x slower                                                  |
| fannkuch                | 388 ms                                                 | 467 ms: 1.20x slower                                                   |
| float                   | 76.3 ms                                                | 107 ms: 1.40x slower                                                   |
| generators              | 72.2 ms                                                | 61.6 ms: 1.17x faster                                                  |
| genshi_text             | 22.1 ms                                                | 30.1 ms: 1.36x slower                                                  |
| genshi_xml              | 52.1 ms                                                | 63.2 ms: 1.21x slower                                                  |
| go                      | 143 ms                                                 | 224 ms: 1.56x slower                                                   |
| hexiom                  | 6.35 ms                                                | 9.25 ms: 1.46x slower                                                  |
| html5lib                | 63.2 ms                                                | 86.5 ms: 1.37x slower                                                  |
| json                    | 4.95 ms                                                | 5.26 ms: 1.06x slower                                                  |
| json_dumps              | 12.7 ms                                                | 13.7 ms: 1.08x slower                                                  |
| json_loads              | 26.2 us                                                | 28.4 us: 1.08x slower                                                  |
| logging_format          | 6.62 us                                                | 8.72 us: 1.32x slower                                                  |
| logging_silent          | 98.5 ns                                                | 169 ns: 1.71x slower                                                   |
| logging_simple          | 6.06 us                                                | 8.01 us: 1.32x slower                                                  |
| mako                    | 9.85 ms                                                | 14.7 ms: 1.49x slower                                                  |
| mdp                     | 2.62 sec                                               | 2.82 sec: 1.08x slower                                                 |
| meteor_contest          | 105 ms                                                 | 111 ms: 1.06x slower                                                   |
| nbody                   | 95.0 ms                                                | 141 ms: 1.48x slower                                                   |
| nqueens                 | 85.0 ms                                                | 97.2 ms: 1.14x slower                                                  |
| pathlib                 | 18.2 ms                                                | 18.9 ms: 1.04x slower                                                  |
| pickle                  | 9.79 us                                                | 10.0 us: 1.03x slower                                                  |
| pickle_dict             | 31.4 us                                                | 26.9 us: 1.17x faster                                                  |
| pickle_list             | 4.17 us                                                | 4.45 us: 1.07x slower                                                  |
| pickle_pure_python      | 304 us                                                 | 451 us: 1.48x slower                                                   |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                                   |
| pprint_safe_repr        | 691 ms                                                 | 938 ms: 1.36x slower                                                   |
| pprint_pformat          | 1.44 sec                                               | 1.94 sec: 1.34x slower                                                 |
| pycparser               | 1.17 sec                                               | 1.52 sec: 1.30x slower                                                 |
| pyflate                 | 417 ms                                                 | 660 ms: 1.58x slower                                                   |
| pylint                  | 463 ms                                                 | 512 ms: 1.11x slower                                                   |
| python_startup          | 8.36 ms                                                | 15.2 ms: 1.82x slower                                                  |
| python_startup_no_site  | 5.96 ms                                                | 5.79 ms: 1.03x faster                                                  |
| raytrace                | 290 ms                                                 | 466 ms: 1.60x slower                                                   |
| regex_compile           | 136 ms                                                 | 171 ms: 1.26x slower                                                   |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                   |
| regex_effbot            | 3.36 ms                                                | 3.24 ms: 1.04x faster                                                  |
| regex_v8                | 22.3 ms                                                | 25.4 ms: 1.14x slower                                                  |
| richards                | 46.2 ms                                                | 72.6 ms: 1.57x slower                                                  |
| scimark_fft             | 329 ms                                                 | 411 ms: 1.25x slower                                                   |
| scimark_lu              | 107 ms                                                 | 160 ms: 1.49x slower                                                   |
| scimark_monte_carlo     | 68.3 ms                                                | 106 ms: 1.56x slower                                                   |
| scimark_sor             | 115 ms                                                 | 195 ms: 1.69x slower                                                   |
| scimark_sparse_mat_mult | 4.40 ms                                                | 5.44 ms: 1.24x slower                                                  |
| spectral_norm           | 99.9 ms                                                | 149 ms: 1.49x slower                                                   |
| sqlglot_parse           | 1.37 ms                                                | 2.57 ms: 1.87x slower                                                  |
| sqlglot_transpile       | 1.66 ms                                                | 2.97 ms: 1.79x slower                                                  |
| sqlglot_optimize        | 53.0 ms                                                | 66.1 ms: 1.25x slower                                                  |
| sqlglot_normalize       | 108 ms                                                 | 135 ms: 1.25x slower                                                   |
| sqlite_synth            | 2.49 us                                                | 2.94 us: 1.18x slower                                                  |
| sympy_expand            | 472 ms                                                 | 531 ms: 1.13x slower                                                   |
| sympy_integrate         | 20.9 ms                                                | 23.9 ms: 1.15x slower                                                  |
| sympy_sum               | 166 ms                                                 | 183 ms: 1.10x slower                                                   |
| sympy_str               | 287 ms                                                 | 322 ms: 1.12x slower                                                   |
| telco                   | 6.62 ms                                                | 6.74 ms: 1.02x slower                                                  |
| thrift                  | 752 us                                                 | 1.01 ms: 1.34x slower                                                  |
| tornado_http            | 96.6 ms                                                | 129 ms: 1.34x slower                                                   |
| unpack_sequence         | 43.4 ns                                                | 59.0 ns: 1.36x slower                                                  |
| unpickle                | 13.3 us                                                | 14.3 us: 1.08x slower                                                  |
| unpickle_list           | 4.95 us                                                | 5.01 us: 1.01x slower                                                  |
| unpickle_pure_python    | 225 us                                                 | 294 us: 1.30x slower                                                   |
| xml_etree_parse         | 158 ms                                                 | 154 ms: 1.03x faster                                                   |
| xml_etree_iterparse     | 103 ms                                                 | 110 ms: 1.07x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 92.4 ms: 1.21x slower                                                  |
| xml_etree_process       | 53.8 ms                                                | 73.2 ms: 1.36x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.25x slower                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20210503-3.10.0a7+-d3b9134/bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal
