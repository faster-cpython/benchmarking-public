
# Results vs. 3.10.4

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: darwin-arm64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 161 ms: 1.25x faster                                                   |
| chameleon      | 5.79 ms                                                | 4.45 ms: 1.30x faster                                                  |
| docutils       | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| html5lib       | 44.2 ms                                                | 34.6 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                  |
| float          | 72.4 ms                                                | 52.5 ms: 1.38x faster                                                  |
| pidigits       | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 73.9 ms: 1.30x faster                                                  |
| regex_v8       | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| regex_dna      | 162 ms                                                 | 150 ms: 1.08x faster                                                   |
| regex_effbot   | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 283 us                                                 | 198 us: 1.43x faster                                                   |
| json_dumps           | 8.40 ms                                                | 6.21 ms: 1.35x faster                                                  |
| unpickle_pure_python | 203 us                                                 | 156 us: 1.31x faster                                                   |
| xml_etree_process    | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                  |
| xml_etree_generate   | 54.2 ms                                                | 47.6 ms: 1.14x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 72.3 ms                                                | 69.2 ms: 1.04x faster                                                  |
| unpickle_list        | 2.69 us                                                | 2.58 us: 1.04x faster                                                  |
| json_loads           | 16.9 us                                                | 16.3 us: 1.04x faster                                                  |
| unpickle             | 9.89 us                                                | 9.67 us: 1.02x faster                                                  |
| pickle               | 7.35 us                                                | 7.52 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| python_startup_no_site | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 10.5 ms                                                | 7.99 ms: 1.31x faster                                                  |
| django_template | 27.3 ms                                                | 20.8 ms: 1.31x faster                                                  |
| genshi_xml      | 37.2 ms                                                | 28.7 ms: 1.29x faster                                                  |
| genshi_text     | 18.4 ms                                                | 15.0 ms: 1.22x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-darwin-arm64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 5.14 ms                                                | 2.55 ms: 2.02x faster                                                  |
| logging_silent          | 119 ns                                                 | 63.3 ns: 1.89x faster                                                  |
| richards                | 51.4 ms                                                | 29.3 ms: 1.76x faster                                                  |
| scimark_sor             | 126 ms                                                 | 78.2 ms: 1.61x faster                                                  |
| raytrace                | 325 ms                                                 | 204 ms: 1.60x faster                                                   |
| scimark_monte_carlo     | 72.5 ms                                                | 47.2 ms: 1.54x faster                                                  |
| scimark_lu              | 109 ms                                                 | 71.3 ms: 1.53x faster                                                  |
| go                      | 165 ms                                                 | 108 ms: 1.53x faster                                                   |
| crypto_pyaes            | 78.1 ms                                                | 52.7 ms: 1.48x faster                                                  |
| async_tree_memoization  | 490 ms                                                 | 331 ms: 1.48x faster                                                   |
| nbody                   | 93.3 ms                                                | 64.0 ms: 1.46x faster                                                  |
| sqlglot_parse           | 1.37 ms                                                | 951 us: 1.44x faster                                                   |
| pickle_pure_python      | 283 us                                                 | 198 us: 1.43x faster                                                   |
| sqlglot_transpile       | 1.57 ms                                                | 1.12 ms: 1.41x faster                                                  |
| pyflate                 | 453 ms                                                 | 327 ms: 1.38x faster                                                   |
| float                   | 72.4 ms                                                | 52.5 ms: 1.38x faster                                                  |
| async_tree_none         | 400 ms                                                 | 291 ms: 1.37x faster                                                   |
| async_tree_io           | 1.02 sec                                               | 747 ms: 1.36x faster                                                   |
| pycparser               | 916 ms                                                 | 672 ms: 1.36x faster                                                   |
| json_dumps              | 8.40 ms                                                | 6.21 ms: 1.35x faster                                                  |
| hexiom                  | 6.32 ms                                                | 4.68 ms: 1.35x faster                                                  |
| logging_simple          | 4.63 us                                                | 3.44 us: 1.35x faster                                                  |
| chaos                   | 66.7 ms                                                | 49.6 ms: 1.34x faster                                                  |
| thrift                  | 580 us                                                 | 433 us: 1.34x faster                                                   |
| logging_format          | 4.97 us                                                | 3.74 us: 1.33x faster                                                  |
| spectral_norm           | 95.8 ms                                                | 72.6 ms: 1.32x faster                                                  |
| mako                    | 10.5 ms                                                | 7.99 ms: 1.31x faster                                                  |
| django_template         | 27.3 ms                                                | 20.8 ms: 1.31x faster                                                  |
| unpickle_pure_python    | 203 us                                                 | 156 us: 1.31x faster                                                   |
| regex_compile           | 96.4 ms                                                | 73.9 ms: 1.30x faster                                                  |
| chameleon               | 5.79 ms                                                | 4.45 ms: 1.30x faster                                                  |
| genshi_xml              | 37.2 ms                                                | 28.7 ms: 1.29x faster                                                  |
| xml_etree_process       | 44.8 ms                                                | 34.7 ms: 1.29x faster                                                  |
| html5lib                | 44.2 ms                                                | 34.6 ms: 1.28x faster                                                  |
| create_gc_cycles        | 880 us                                                 | 692 us: 1.27x faster                                                   |
| pprint_safe_repr        | 606 ms                                                 | 480 ms: 1.26x faster                                                   |
| pprint_pformat          | 1.23 sec                                               | 978 ms: 1.26x faster                                                   |
| 2to3                    | 201 ms                                                 | 161 ms: 1.25x faster                                                   |
| dulwich_log             | 37.1 ms                                                | 29.7 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult | 3.46 ms                                                | 2.79 ms: 1.24x faster                                                  |
| deepcopy_memo           | 34.4 us                                                | 28.0 us: 1.23x faster                                                  |
| fannkuch                | 317 ms                                                 | 259 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed | 669 ms                                                 | 547 ms: 1.22x faster                                                   |
| genshi_text             | 18.4 ms                                                | 15.0 ms: 1.22x faster                                                  |
| docutils                | 1.78 sec                                               | 1.46 sec: 1.22x faster                                                 |
| deepcopy                | 281 us                                                 | 232 us: 1.21x faster                                                   |
| sqlglot_optimize        | 38.0 ms                                                | 31.6 ms: 1.20x faster                                                  |
| deepcopy_reduce         | 2.37 us                                                | 1.99 us: 1.19x faster                                                  |
| bench_thread_pool       | 546 us                                                 | 458 us: 1.19x faster                                                   |
| scimark_fft             | 230 ms                                                 | 194 ms: 1.19x faster                                                   |
| dask                    | 265 ms                                                 | 225 ms: 1.18x faster                                                   |
| mypy2                   | 307 ms                                                 | 262 ms: 1.17x faster                                                   |
| async_generators        | 234 ms                                                 | 201 ms: 1.16x faster                                                   |
| sympy_integrate         | 13.3 ms                                                | 11.5 ms: 1.16x faster                                                  |
| unpack_sequence         | 37.4 ns                                                | 32.8 ns: 1.14x faster                                                  |
| sqlglot_normalize       | 196 ms                                                 | 172 ms: 1.14x faster                                                   |
| xml_etree_generate      | 54.2 ms                                                | 47.6 ms: 1.14x faster                                                  |
| sympy_expand            | 275 ms                                                 | 244 ms: 1.13x faster                                                   |
| nqueens                 | 68.2 ms                                                | 60.4 ms: 1.13x faster                                                  |
| regex_v8                | 17.6 ms                                                | 15.7 ms: 1.12x faster                                                  |
| sympy_str               | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| xml_etree_parse         | 106 ms                                                 | 96.3 ms: 1.11x faster                                                  |
| json                    | 3.08 ms                                                | 2.80 ms: 1.10x faster                                                  |
| mdp                     | 1.66 sec                                               | 1.51 sec: 1.10x faster                                                 |
| coroutines              | 20.2 ms                                                | 18.4 ms: 1.10x faster                                                  |
| sympy_sum               | 93.6 ms                                                | 86.6 ms: 1.08x faster                                                  |
| regex_dna               | 162 ms                                                 | 150 ms: 1.08x faster                                                   |
| telco                   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                  |
| comprehensions          | 17.6 us                                                | 16.6 us: 1.06x faster                                                  |
| pathlib                 | 28.8 ms                                                | 27.5 ms: 1.05x faster                                                  |
| xml_etree_iterparse     | 72.3 ms                                                | 69.2 ms: 1.04x faster                                                  |
| unpickle_list           | 2.69 us                                                | 2.58 us: 1.04x faster                                                  |
| json_loads              | 16.9 us                                                | 16.3 us: 1.04x faster                                                  |
| sqlite_synth            | 1.47 us                                                | 1.44 us: 1.03x faster                                                  |
| unpickle                | 9.89 us                                                | 9.67 us: 1.02x faster                                                  |
| meteor_contest          | 78.1 ms                                                | 76.4 ms: 1.02x faster                                                  |
| asyncio_tcp             | 670 ms                                                 | 665 ms: 1.01x faster                                                   |
| pidigits                | 282 ms                                                 | 281 ms: 1.01x faster                                                   |
| gc_traversal            | 2.39 ms                                                | 2.41 ms: 1.01x slower                                                  |
| pickle                  | 7.35 us                                                | 7.52 us: 1.02x slower                                                  |
| python_startup          | 11.9 ms                                                | 12.2 ms: 1.03x slower                                                  |
| regex_effbot            | 2.46 ms                                                | 2.62 ms: 1.07x slower                                                  |
| bench_mp_pool           | 39.7 ms                                                | 44.2 ms: 1.11x slower                                                  |
| python_startup_no_site  | 8.88 ms                                                | 10.3 ms: 1.16x slower                                                  |
| coverage                | 42.0 ms                                                | 58.6 ms: 1.39x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (3): generators, pickle_dict, pickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
