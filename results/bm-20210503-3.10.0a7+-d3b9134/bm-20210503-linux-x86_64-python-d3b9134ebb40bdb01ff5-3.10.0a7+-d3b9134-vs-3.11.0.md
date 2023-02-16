
# Results vs. 3.11.0

- fork: python
- ref: d3b9134ebb40bdb01ff5
- machine: linux-x86_64
- commit hash: d3b9134
- commit date: 2021-05-03
- overall geometric mean: 1.24x slower \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 333 ms: 1.29x slower                                                   |
| docutils       | 2.60 sec                                               | 3.17 sec: 1.22x slower                                                 |
| html5lib       | 64.8 ms                                                | 86.5 ms: 1.33x slower                                                  |
| tornado_http   | 96.5 ms                                                | 129 ms: 1.34x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 197 ms                                                 | 190 ms: 1.04x faster                                                   |
| float          | 76.8 ms                                                | 107 ms: 1.39x slower                                                   |
| nbody          | 90.0 ms                                                | 141 ms: 1.57x slower                                                   |
| Geometric mean | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.46 ms                                                | 3.24 ms: 1.07x faster                                                  |
| regex_dna      | 203 ms                                                 | 211 ms: 1.04x slower                                                   |
| regex_v8       | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                  |
| regex_compile  | 136 ms                                                 | 171 ms: 1.25x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_dict          | 31.2 us                                                | 26.9 us: 1.16x faster                                                  |
| xml_etree_parse      | 160 ms                                                 | 154 ms: 1.04x faster                                                   |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 110 ms: 1.06x slower                                                   |
| pickle_list          | 4.14 us                                                | 4.45 us: 1.07x slower                                                  |
| unpickle             | 13.3 us                                                | 14.3 us: 1.08x slower                                                  |
| json_loads           | 26.1 us                                                | 28.4 us: 1.09x slower                                                  |
| json_dumps           | 12.4 ms                                                | 13.7 ms: 1.11x slower                                                  |
| xml_etree_generate   | 75.9 ms                                                | 92.4 ms: 1.22x slower                                                  |
| unpickle_pure_python | 227 us                                                 | 294 us: 1.29x slower                                                   |
| xml_etree_process    | 53.7 ms                                                | 73.2 ms: 1.36x slower                                                  |
| pickle_pure_python   | 308 us                                                 | 451 us: 1.46x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 5.79 ms: 1.04x faster                                                  |
| python_startup         | 8.58 ms                                                | 15.2 ms: 1.78x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.30x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 63.2 ms: 1.23x slower                                                  |
| genshi_text     | 21.5 ms                                                | 30.1 ms: 1.40x slower                                                  |
| django_template | 32.3 ms                                                | 46.2 ms: 1.43x slower                                                  |
| mako            | 9.83 ms                                                | 14.7 ms: 1.49x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.38x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20210503-linux-x86_64-python-d3b9134ebb40bdb01ff5-3.10.0a7+-d3b9134 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coverage                | 99.3 ms                                                | 65.8 ms: 1.51x faster                                                  |
| generators              | 73.5 ms                                                | 61.6 ms: 1.19x faster                                                  |
| pickle_dict             | 31.2 us                                                | 26.9 us: 1.16x faster                                                  |
| gc_traversal            | 3.82 ms                                                | 3.48 ms: 1.10x faster                                                  |
| regex_effbot            | 3.46 ms                                                | 3.24 ms: 1.07x faster                                                  |
| python_startup_no_site  | 6.04 ms                                                | 5.79 ms: 1.04x faster                                                  |
| xml_etree_parse         | 160 ms                                                 | 154 ms: 1.04x faster                                                   |
| pidigits                | 197 ms                                                 | 190 ms: 1.04x faster                                                   |
| asyncio_tcp             | 883 ms                                                 | 893 ms: 1.01x slower                                                   |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                                  |
| regex_dna               | 203 ms                                                 | 211 ms: 1.04x slower                                                   |
| pathlib                 | 18.1 ms                                                | 18.9 ms: 1.05x slower                                                  |
| telco                   | 6.43 ms                                                | 6.74 ms: 1.05x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 110 ms: 1.06x slower                                                   |
| meteor_contest          | 104 ms                                                 | 111 ms: 1.06x slower                                                   |
| mdp                     | 2.63 sec                                               | 2.82 sec: 1.07x slower                                                 |
| pickle_list             | 4.14 us                                                | 4.45 us: 1.07x slower                                                  |
| json                    | 4.87 ms                                                | 5.26 ms: 1.08x slower                                                  |
| unpickle                | 13.3 us                                                | 14.3 us: 1.08x slower                                                  |
| json_loads              | 26.1 us                                                | 28.4 us: 1.09x slower                                                  |
| sympy_sum               | 166 ms                                                 | 183 ms: 1.11x slower                                                   |
| create_gc_cycles        | 1.52 ms                                                | 1.67 ms: 1.11x slower                                                  |
| json_dumps              | 12.4 ms                                                | 13.7 ms: 1.11x slower                                                  |
| sympy_str               | 291 ms                                                 | 322 ms: 1.11x slower                                                   |
| pylint                  | 462 ms                                                 | 512 ms: 1.11x slower                                                   |
| djangocms               | 32.5 us                                                | 36.4 us: 1.12x slower                                                  |
| sympy_expand            | 475 ms                                                 | 531 ms: 1.12x slower                                                   |
| sympy_integrate         | 21.0 ms                                                | 23.9 ms: 1.14x slower                                                  |
| regex_v8                | 22.2 ms                                                | 25.4 ms: 1.14x slower                                                  |
| nqueens                 | 83.8 ms                                                | 97.2 ms: 1.16x slower                                                  |
| coroutines              | 26.2 ms                                                | 30.4 ms: 1.16x slower                                                  |
| bench_thread_pool       | 817 us                                                 | 960 us: 1.18x slower                                                   |
| async_generators        | 356 ms                                                 | 420 ms: 1.18x slower                                                   |
| dulwich_log             | 64.0 ms                                                | 75.6 ms: 1.18x slower                                                  |
| sqlite_synth            | 2.48 us                                                | 2.94 us: 1.19x slower                                                  |
| scimark_sparse_mat_mult | 4.59 ms                                                | 5.44 ms: 1.19x slower                                                  |
| fannkuch                | 384 ms                                                 | 467 ms: 1.22x slower                                                   |
| xml_etree_generate      | 75.9 ms                                                | 92.4 ms: 1.22x slower                                                  |
| docutils                | 2.60 sec                                               | 3.17 sec: 1.22x slower                                                 |
| genshi_xml              | 51.4 ms                                                | 63.2 ms: 1.23x slower                                                  |
| deepcopy_reduce         | 3.02 us                                                | 3.73 us: 1.24x slower                                                  |
| deepcopy                | 341 us                                                 | 423 us: 1.24x slower                                                   |
| regex_compile           | 136 ms                                                 | 171 ms: 1.25x slower                                                   |
| sqlglot_optimize        | 52.7 ms                                                | 66.1 ms: 1.25x slower                                                  |
| sqlglot_normalize       | 108 ms                                                 | 135 ms: 1.26x slower                                                   |
| scimark_fft             | 325 ms                                                 | 411 ms: 1.26x slower                                                   |
| pycparser               | 1.19 sec                                               | 1.52 sec: 1.28x slower                                                 |
| 2to3                    | 259 ms                                                 | 333 ms: 1.29x slower                                                   |
| unpickle_pure_python    | 227 us                                                 | 294 us: 1.29x slower                                                   |
| unpack_sequence         | 44.5 ns                                                | 59.0 ns: 1.33x slower                                                  |
| async_tree_cpu_io_mixed | 736 ms                                                 | 977 ms: 1.33x slower                                                   |
| pprint_safe_repr        | 706 ms                                                 | 938 ms: 1.33x slower                                                   |
| thrift                  | 760 us                                                 | 1.01 ms: 1.33x slower                                                  |
| logging_simple          | 6.02 us                                                | 8.01 us: 1.33x slower                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.94 sec: 1.33x slower                                                 |
| html5lib                | 64.8 ms                                                | 86.5 ms: 1.33x slower                                                  |
| tornado_http            | 96.5 ms                                                | 129 ms: 1.34x slower                                                   |
| logging_format          | 6.48 us                                                | 8.72 us: 1.35x slower                                                  |
| async_tree_none         | 526 ms                                                 | 712 ms: 1.35x slower                                                   |
| async_tree_memoization  | 624 ms                                                 | 848 ms: 1.36x slower                                                   |
| deepcopy_memo           | 35.8 us                                                | 48.8 us: 1.36x slower                                                  |
| xml_etree_process       | 53.7 ms                                                | 73.2 ms: 1.36x slower                                                  |
| async_tree_io           | 1.30 sec                                               | 1.80 sec: 1.38x slower                                                 |
| float                   | 76.8 ms                                                | 107 ms: 1.39x slower                                                   |
| genshi_text             | 21.5 ms                                                | 30.1 ms: 1.40x slower                                                  |
| django_template         | 32.3 ms                                                | 46.2 ms: 1.43x slower                                                  |
| hexiom                  | 6.34 ms                                                | 9.25 ms: 1.46x slower                                                  |
| pickle_pure_python      | 308 us                                                 | 451 us: 1.46x slower                                                   |
| scimark_lu              | 108 ms                                                 | 160 ms: 1.48x slower                                                   |
| mako                    | 9.83 ms                                                | 14.7 ms: 1.49x slower                                                  |
| spectral_norm           | 98.1 ms                                                | 149 ms: 1.52x slower                                                   |
| chaos                   | 68.7 ms                                                | 106 ms: 1.55x slower                                                   |
| crypto_pyaes            | 75.7 ms                                                | 118 ms: 1.55x slower                                                   |
| scimark_monte_carlo     | 68.0 ms                                                | 106 ms: 1.56x slower                                                   |
| nbody                   | 90.0 ms                                                | 141 ms: 1.57x slower                                                   |
| richards                | 46.1 ms                                                | 72.6 ms: 1.57x slower                                                  |
| pyflate                 | 419 ms                                                 | 660 ms: 1.58x slower                                                   |
| go                      | 140 ms                                                 | 224 ms: 1.59x slower                                                   |
| raytrace                | 291 ms                                                 | 466 ms: 1.60x slower                                                   |
| scimark_sor             | 115 ms                                                 | 195 ms: 1.69x slower                                                   |
| logging_silent          | 98.0 ns                                                | 169 ns: 1.72x slower                                                   |
| python_startup          | 8.58 ms                                                | 15.2 ms: 1.78x slower                                                  |
| sqlglot_transpile       | 1.65 ms                                                | 2.97 ms: 1.80x slower                                                  |
| sqlglot_parse           | 1.36 ms                                                | 2.57 ms: 1.89x slower                                                  |
| deltablue               | 3.66 ms                                                | 7.29 ms: 1.99x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.24x slower                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
