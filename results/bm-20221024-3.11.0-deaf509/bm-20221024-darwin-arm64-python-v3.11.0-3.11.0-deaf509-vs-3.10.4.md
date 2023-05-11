
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: darwin-arm64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.21x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| chameleon      | 5.79 ms                                                | 4.60 ms: 1.26x faster                                  |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                 |
| html5lib       | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| tornado_http   | 91.5 ms                                                | 71.5 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 65.6 ms: 1.42x faster                                  |
| float          | 72.4 ms                                                | 53.0 ms: 1.37x faster                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 76.7 ms: 1.26x faster                                  |
| regex_v8       | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| regex_dna      | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| regex_effbot   | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 201 us: 1.41x faster                                   |
| xml_etree_process    | 44.8 ms                                                | 35.1 ms: 1.28x faster                                  |
| unpickle_pure_python | 203 us                                                 | 159 us: 1.28x faster                                   |
| xml_etree_generate   | 54.2 ms                                                | 48.3 ms: 1.12x faster                                  |
| json_dumps           | 8.40 ms                                                | 7.63 ms: 1.10x faster                                  |
| json_loads           | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 70.1 ms: 1.03x faster                                  |
| pickle               | 7.35 us                                                | 7.15 us: 1.03x faster                                  |
| unpickle             | 9.89 us                                                | 9.67 us: 1.02x faster                                  |
| unpickle_list        | 2.69 us                                                | 2.65 us: 1.01x faster                                  |
| pickle_dict          | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.4 ms: 1.04x slower                                  |
| python_startup_no_site | 8.88 ms                                                | 10.2 ms: 1.14x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 27.3 ms                                                | 21.0 ms: 1.30x faster                                  |
| genshi_xml      | 37.2 ms                                                | 29.8 ms: 1.25x faster                                  |
| mako            | 10.5 ms                                                | 8.53 ms: 1.23x faster                                  |
| genshi_text     | 18.4 ms                                                | 15.3 ms: 1.20x faster                                  |
| Geometric mean  | (ref)                                                  | 1.24x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.81 ms: 1.83x faster                                  |
| logging_silent          | 119 ns                                                 | 68.1 ns: 1.75x faster                                  |
| richards                | 51.4 ms                                                | 32.2 ms: 1.60x faster                                  |
| mypy2                   | 307 ms                                                 | 195 ms: 1.57x faster                                   |
| raytrace                | 325 ms                                                 | 207 ms: 1.57x faster                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 46.5 ms: 1.56x faster                                  |
| scimark_sor             | 126 ms                                                 | 82.6 ms: 1.53x faster                                  |
| go                      | 165 ms                                                 | 109 ms: 1.52x faster                                   |
| crypto_pyaes            | 78.1 ms                                                | 51.7 ms: 1.51x faster                                  |
| scimark_lu              | 109 ms                                                 | 73.3 ms: 1.49x faster                                  |
| pyflate                 | 453 ms                                                 | 310 ms: 1.46x faster                                   |
| async_tree_memoization  | 490 ms                                                 | 336 ms: 1.46x faster                                   |
| async_tree_io           | 1.02 sec                                               | 704 ms: 1.45x faster                                   |
| sqlglot_parse           | 1.37 ms                                                | 959 us: 1.42x faster                                   |
| nbody                   | 93.3 ms                                                | 65.6 ms: 1.42x faster                                  |
| pickle_pure_python      | 283 us                                                 | 201 us: 1.41x faster                                   |
| async_tree_none         | 400 ms                                                 | 286 ms: 1.40x faster                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.12 ms: 1.40x faster                                  |
| float                   | 72.4 ms                                                | 53.0 ms: 1.37x faster                                  |
| chaos                   | 66.7 ms                                                | 49.4 ms: 1.35x faster                                  |
| hexiom                  | 6.32 ms                                                | 4.72 ms: 1.34x faster                                  |
| spectral_norm           | 95.8 ms                                                | 72.6 ms: 1.32x faster                                  |
| logging_format          | 4.97 us                                                | 3.78 us: 1.31x faster                                  |
| thrift                  | 580 us                                                 | 442 us: 1.31x faster                                   |
| pycparser               | 916 ms                                                 | 698 ms: 1.31x faster                                   |
| deepcopy_memo           | 34.4 us                                                | 26.3 us: 1.31x faster                                  |
| logging_simple          | 4.63 us                                                | 3.55 us: 1.30x faster                                  |
| pprint_safe_repr        | 606 ms                                                 | 466 ms: 1.30x faster                                   |
| django_template         | 27.3 ms                                                | 21.0 ms: 1.30x faster                                  |
| pprint_pformat          | 1.23 sec                                               | 954 ms: 1.29x faster                                   |
| tornado_http            | 91.5 ms                                                | 71.5 ms: 1.28x faster                                  |
| xml_etree_process       | 44.8 ms                                                | 35.1 ms: 1.28x faster                                  |
| unpickle_pure_python    | 203 us                                                 | 159 us: 1.28x faster                                   |
| html5lib                | 44.2 ms                                                | 34.7 ms: 1.27x faster                                  |
| deepcopy                | 281 us                                                 | 223 us: 1.26x faster                                   |
| chameleon               | 5.79 ms                                                | 4.60 ms: 1.26x faster                                  |
| regex_compile           | 96.4 ms                                                | 76.7 ms: 1.26x faster                                  |
| async_tree_cpu_io_mixed | 669 ms                                                 | 533 ms: 1.25x faster                                   |
| genshi_xml              | 37.2 ms                                                | 29.8 ms: 1.25x faster                                  |
| 2to3                    | 201 ms                                                 | 161 ms: 1.25x faster                                   |
| deepcopy_reduce         | 2.37 us                                                | 1.91 us: 1.24x faster                                  |
| sqlalchemy_imperative   | 8.89 ms                                                | 7.20 ms: 1.23x faster                                  |
| create_gc_cycles        | 880 us                                                 | 716 us: 1.23x faster                                   |
| mako                    | 10.5 ms                                                | 8.53 ms: 1.23x faster                                  |
| dulwich_log             | 37.1 ms                                                | 30.3 ms: 1.22x faster                                  |
| sqlglot_optimize        | 38.0 ms                                                | 31.1 ms: 1.22x faster                                  |
| fannkuch                | 317 ms                                                 | 261 ms: 1.21x faster                                   |
| gunicorn                | 1.35 ms                                                | 1.11 ms: 1.21x faster                                  |
| aiohttp                 | 1.27 ms                                                | 1.05 ms: 1.21x faster                                  |
| docutils                | 1.78 sec                                               | 1.47 sec: 1.21x faster                                 |
| genshi_text             | 18.4 ms                                                | 15.3 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 74.9 ms                                                | 62.6 ms: 1.20x faster                                  |
| async_generators        | 234 ms                                                 | 196 ms: 1.19x faster                                   |
| sqlite_synth            | 1.47 us                                                | 1.27 us: 1.16x faster                                  |
| scimark_fft             | 230 ms                                                 | 200 ms: 1.15x faster                                   |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.15x faster                                  |
| bench_thread_pool       | 546 us                                                 | 474 us: 1.15x faster                                   |
| sqlglot_normalize       | 196 ms                                                 | 171 ms: 1.15x faster                                   |
| nqueens                 | 68.2 ms                                                | 59.8 ms: 1.14x faster                                  |
| sympy_expand            | 275 ms                                                 | 242 ms: 1.14x faster                                   |
| generators              | 32.7 ms                                                | 28.8 ms: 1.14x faster                                  |
| coroutines              | 20.2 ms                                                | 17.8 ms: 1.13x faster                                  |
| flaskblogging           | 2.75 ms                                                | 2.43 ms: 1.13x faster                                  |
| pylint                  | 307 ms                                                 | 272 ms: 1.13x faster                                   |
| xml_etree_generate      | 54.2 ms                                                | 48.3 ms: 1.12x faster                                  |
| sympy_str               | 169 ms                                                 | 151 ms: 1.12x faster                                   |
| json                    | 3.08 ms                                                | 2.78 ms: 1.11x faster                                  |
| json_dumps              | 8.40 ms                                                | 7.63 ms: 1.10x faster                                  |
| unpack_sequence         | 37.4 ns                                                | 34.1 ns: 1.10x faster                                  |
| sympy_sum               | 93.6 ms                                                | 85.5 ms: 1.09x faster                                  |
| comprehensions          | 17.6 us                                                | 16.1 us: 1.09x faster                                  |
| regex_v8                | 17.6 ms                                                | 16.1 ms: 1.09x faster                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.19 ms: 1.08x faster                                  |
| mdp                     | 1.66 sec                                               | 1.55 sec: 1.08x faster                                 |
| telco                   | 3.63 ms                                                | 3.41 ms: 1.07x faster                                  |
| regex_dna               | 162 ms                                                 | 152 ms: 1.06x faster                                   |
| meteor_contest          | 78.1 ms                                                | 73.5 ms: 1.06x faster                                  |
| pathlib                 | 28.8 ms                                                | 27.2 ms: 1.06x faster                                  |
| json_loads              | 16.9 us                                                | 16.1 us: 1.05x faster                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 70.1 ms: 1.03x faster                                  |
| pickle                  | 7.35 us                                                | 7.15 us: 1.03x faster                                  |
| asyncio_tcp             | 670 ms                                                 | 651 ms: 1.03x faster                                   |
| unpickle                | 9.89 us                                                | 9.67 us: 1.02x faster                                  |
| unpickle_list           | 2.69 us                                                | 2.65 us: 1.01x faster                                  |
| pidigits                | 282 ms                                                 | 281 ms: 1.00x faster                                   |
| pickle_dict             | 17.9 us                                                | 18.0 us: 1.00x slower                                  |
| gc_traversal            | 2.39 ms                                                | 2.42 ms: 1.01x slower                                  |
| xml_etree_parse         | 106 ms                                                 | 108 ms: 1.02x slower                                   |
| python_startup          | 11.9 ms                                                | 12.4 ms: 1.04x slower                                  |
| regex_effbot            | 2.46 ms                                                | 2.63 ms: 1.07x slower                                  |
| bench_mp_pool           | 39.7 ms                                                | 43.9 ms: 1.11x slower                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.2 ms: 1.14x slower                                  |
| coverage                | 42.0 ms                                                | 58.4 ms: 1.39x slower                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                           |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: dask
Ignored benchmarks (4) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols
